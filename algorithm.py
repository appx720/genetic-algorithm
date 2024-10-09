import random
import copy


def create(c, l) -> list:
    """
    :param c: The count of created binary string
    :param l: The length of each binary string
    :return: A list of binary string
    """
    created = []

    for i in range(c):
        s = "".join(str(random.randint(0, 1)) for _ in range(l))
        created.append(s)
    
    return created


def find_superior(group, count):
    """
    :param group: The target group to find superior genes in
    :param count: The number of superior genes to find
    :return: A list of superior genes
    """
    superior_group = []
    sorted_group = sorted(group, key = lambda x: x.count("1"), reverse=True) # sorted func to optimize
    
    for gene in sorted_group:
        if len(superior_group) < count:
            superior_group.append(gene)
        else:
            break
    
    if len(superior_group) > count:
        superior_group = random.sample(superior_group, count)
    
    return superior_group


def mate(group):
    """
    :param group: The group to mate in
    :return: A mated group
    """
    n_group = []

    while len(n_group) < len(group):
        m_group = random.sample(group, 2)
        n_gene = "".join(random.choice([m_group[0][j], m_group[1][j]]) for j in range(len(m_group[0])))
        n_group.append(n_gene)

    return n_group


def confront(group, count):
    """
    :param group: The target group to confront in
    :param count: The number of elements to return
    :return: A list of elements after confrontation
    """
    group = mate(group)
    n_group = random.sample(group, count)
    return n_group


def mutation(group):
    """
    :param group: The group to mutate in
    :return: A mutated group
    """
    for i in range(len(group)):
        if random.random() < 0.001:  # 0.1% to mutate
            gene_list = list(group[i])

            for j in range(len(gene_list)):
                if random.random() < 0.1:  # 10% to change each bits
                    gene_list[j] = str(random.randint(0, 1))
            
            group[i] = ''.join(gene_list)
    
    return group



def algorithm(bit_size, group_size, superior_size, rorate) -> list:
    final_group = [] # old, new

    g = create(group_size, bit_size)
    final_group.append(g)

    for _ in range(rorate):
        group = copy.deepcopy(g)

        superior = find_superior(group, superior_size)
        m_group = mate(superior)

        g = confront(g, group_size)
        g += m_group
        g = mutation(g)


    final_group.append(g)
    return final_group