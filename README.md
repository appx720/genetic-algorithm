# Genetic Algorithm Implementation and Analysis

This repository contains a Python implementation of a Genetic Algorithm (GA) designed to solve optimization problems. The GA is enhanced with an analysis feature that evaluates various parameter combinations and saves the results in JSON format for further inspection.

If you want to get more information about the algorithm, please refer to the `algorithm.md` file.

## Features

- **Genetic Algorithm**: Implements selection, crossover, and mutation operations to evolve a population of candidate solutions.
- **Parameter Analysis**: Automatically tests different combinations of parameters such as bit size, group size, superior size, and rotation count.
- **JSON Output**: Results of the analysis, including the ratio of '1' bits in the final population, are saved in a structured JSON file for easy access and review.

## Usage

### Running the Algorithm

1. **Run the Algorithm**:
   - You can directly use the genetic algorithm implemented in `algorithm.py`.
   - Execute the following command in your terminal or command prompt:
     ```bash
     python algorithm.py
     ```
   - This will run the genetic algorithm and display the results.

### Analyzing the Algorithm

1. **Prepare for Analysis**:
   - Before running the analysis, ensure that you have set the desired parameters in `analyze.py`.

2. **Run the Analysis**:
   - To analyze the performance of the genetic algorithm, run the following command:
     ```bash
     python analyze.py
     ```
   - This will execute the analysis and generate a JSON file (`analysis.json`) containing the results of various parameter combinations.

3. **View Results**:
   - After running the analysis, open `analysis.json` to review the results, which include metrics such as the ratio of '1' bits in the final population.

### Editing Parameters

- You can modify the parameters for both the algorithm and analysis directly in the respective Python files (`algorithm.py` and `analyze.py`) to suit your testing needs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
