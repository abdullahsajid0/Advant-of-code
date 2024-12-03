import re

def calculate_sum_of_multiplications(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        memory = file.read()
    
    # Regular expression to match valid mul instructions
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Find all matches in the corrupted memory
    matches = re.findall(pattern, memory)
    
    # Perform the multiplications and sum them up
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

# Path to the input file (replace 'input.txt' with your actual file name)
file_path = 'input.txt'

# Calculate the result
result = calculate_sum_of_multiplications(file_path)

print(f"The total sum of valid multiplications is: {result}")
