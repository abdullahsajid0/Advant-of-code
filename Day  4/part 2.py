def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Define all possible MAS patterns (forwards and backwards)
    mas_patterns = {"MAS", "SAM"}

    # Loop through each possible 3x3 sub-grid
    for r in range(rows - 2):
        for c in range(cols - 2):
            # Extract characters in the "X-MAS" shape
            top_left = grid[r][c]
            top_right = grid[r][c + 2]
            center = grid[r + 1][c + 1]
            bottom_left = grid[r + 2][c]
            bottom_right = grid[r + 2][c + 2]

            # Check if the diagonal matches a valid X-MAS pattern
            top_mas = top_left + center + bottom_right
            bottom_mas = bottom_left + center + top_right

            if top_mas in mas_patterns and bottom_mas in mas_patterns:
                count += 1

    return count

# Read the input file
file_path = "input.txt"
with open(file_path, 'r') as file:
    grid = [line.strip() for line in file]

# Count X-MAS occurrences
result = count_x_mas(grid)
print(f"The number of X-MAS patterns is: {result}")
