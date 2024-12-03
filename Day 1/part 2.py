from collections import Counter

# Define a function to read data from a single file and split into two lists
def read_file_to_lists(file_path):
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

# Path to the input file
file_path = 'input.txt'

# Read data from the file
left_list, right_list = read_file_to_lists(file_path)

# Count occurrences of numbers in the right list
right_list_counts = Counter(right_list)

# Calculate the similarity score
similarity_score = sum(num * right_list_counts[num] for num in left_list)

# Output the result
print(f"The similarity score is: {similarity_score}")
