from algorithm import algorithm

import json, os
import itertools
import random


def analyze_algorithm(bit_size_range, group_size_range, superior_size_range, rorate_range, num_cases = 100):    
    """
    Analyze the algorithm and save the result to a json file.

    The function tries all the combinations of parameters, runs the algorithm
    for each combination, and saves the result to a json file. The result is
    represented as a list of dictionaries, each of which contains the parameters
    and the ratio of 1 bits to the total bits.

    Parameters:
        bit_size_range (tuple of int): The range of bit size to try. The tuple
            should contain three elements: the start value, the end value, and
            the step value.
        group_size_range (tuple of int): The range of group size to try.
        superior_size_range (tuple of int): The range of superior size to try.
        rorate_range (tuple of int): The range of rorate to try.
        num_cases (int): The number of times to run the algorithm for each
            combination of parameters. Defaults to 100.
    """
    results = []

    # 모든 매개변수 조합 생성
    param_combinations = itertools.product(
        range(bit_size_range[0], bit_size_range[1] + 1, bit_size_range[2]),
        range(group_size_range[0], group_size_range[1] + 1, group_size_range[2]),
        range(superior_size_range[0], superior_size_range[1] + 1),
        range(rorate_range[0], rorate_range[1] + 1, rorate_range[2])
    )


    for bit_size, group_size, superior_size, rorate in param_combinations:
        total_ones = 0
        total_bits = 0

        for _ in range(num_cases):
            result = algorithm(bit_size, group_size, superior_size, rorate)
            random_result = random.choice(result[1])

            ones_count = random_result.count("1")
            total_ones += ones_count * len(result[1])
            total_bits += bit_size * len(result[1])
        

        ratio = total_ones / total_bits if total_bits > 0 else 0
        
        results.append({
            "bit_size": bit_size,
            "group_size": group_size,
            "superior_size": superior_size,
            "rorate": rorate,
            "ones_ratio": ratio
        })


    if os.path.exists('analysis.json'):
        with open('analysis.json', 'r') as json_file:
            existing_data = json.load(json_file)
        
    else:
        existing_data = []

    existing_data.extend(results)

    with open('analysis.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)



# test set
bit_size_range = [20, 100, 10]
group_size_range = [50, 50, 1]
superior_size_range = [4, 4]
rorate_range = [1000, 1000, 1]


analyze_algorithm(bit_size_range, group_size_range, superior_size_range, rorate_range, num_cases=10)