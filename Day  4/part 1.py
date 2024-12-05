def count_xmas_occurrences(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]
    count = 0

    def is_valid(x, y):
        """Check if coordinates are within grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        """Search for the word starting at (x, y) in direction (dx, dy)."""
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if search_from(r, c, dx, dy):
                    count += 1

    return count

# Read the input file
file_path = "input.txt"
with open(file_path, 'r') as file:
    grid = [line.strip() for line in file]

# Count occurrences of "XMAS"
result = count_xmas_occurrences(grid)
print(f"The word 'XMAS' appears {result} times in the grid.")
