import re

def calculate_enabled_multiplications(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    # Regular expression to match valid mul(X,Y) instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    
    # Regular expression to match do() and don't() instructions
    control_pattern = re.compile(r"do\(\)|don't\(\)")

    # Start with mul instructions enabled
    is_enabled = True
    total = 0

    # Scan the input for matches
    for match in re.finditer(rf"{mul_pattern.pattern}|{control_pattern.pattern}", data):
        instruction = match.group(0)

        if instruction == "do()":
            is_enabled = True
        elif instruction == "don't()":
            is_enabled = False
        else:  # This is a mul(X,Y) instruction
            if is_enabled:
                x, y = map(int, mul_pattern.match(instruction).groups())
                total += x * y

    return total

# Path to the input file
file_path = "input.txt"

# Calculate and print the result
result = calculate_enabled_multiplications(file_path)
print(f"The total sum of enabled multiplications is: {result}")
