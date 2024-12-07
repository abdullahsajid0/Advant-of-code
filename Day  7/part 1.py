from itertools import product

def parse_input(file_path):
    equations = []
    with open(file_path, 'r') as f:
        for line in f:
            target, numbers = line.split(":")
            target = int(target.strip())
            numbers = list(map(int, numbers.strip().split()))
            equations.append((target, numbers))
    return equations

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
    return result

def find_valid_equations(equations):
    valid_targets = []
    for target, numbers in equations:
        num_positions = len(numbers) - 1
        operator_combinations = product(["+", "*"], repeat=num_positions)
        
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == target:
                valid_targets.append(target)
                break  # No need to check further combinations for this equation
    return valid_targets

def main(file_path):
    equations = parse_input(file_path)
    valid_targets = find_valid_equations(equations)
    return sum(valid_targets)

# Example Usage
file_path = "input.txt"  # Replace this with the path to your input file
result = main(file_path)
print(f"Total calibration result: {result}")
