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

# Step 1: Sort both lists
left_list_sorted = sorted(left_list)
right_list_sorted = sorted(right_list)

# Step 2: Compute distances for each pair
distances = [abs(l - r) for l, r in zip(left_list_sorted, right_list_sorted)]

# Step 3: Calculate the total distance
total_distance = sum(distances)

# Output the result
print(f"The total distance is: {total_distance}")
