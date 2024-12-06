def parse_map(file_path):
    with open(file_path, 'r') as file:
        lab_map = [list(line.strip()) for line in file.readlines()]
    
    # Find the initial position and direction of the guard
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    guard_position = None
    guard_direction = None

    for i, row in enumerate(lab_map):
        for j, cell in enumerate(row):
            if cell in directions:
                guard_position = (i, j)
                guard_direction = directions[cell]
                lab_map[i][j] = '.'  # Replace the guard's initial position with empty space
                break
        if guard_position:
            break

    return lab_map, guard_position, guard_direction

def simulate_patrol(lab_map, start_pos, start_dir):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    direction_idx = directions.index(start_dir)
    visited_positions = set()
    current_pos = start_pos

    rows, cols = len(lab_map), len(lab_map[0])

    while True:
        visited_positions.add(current_pos)
        next_row = current_pos[0] + directions[direction_idx][0]
        next_col = current_pos[1] + directions[direction_idx][1]

        # Check if the next position is out of bounds
        if not (0 <= next_row < rows and 0 <= next_col < cols):
            break

        # Check if the next position is an obstacle
        if lab_map[next_row][next_col] == '#':
            direction_idx = (direction_idx + 1) % 4  # Turn right
        else:
            # Move forward
            current_pos = (next_row, next_col)

    return visited_positions

def count_visited_positions(file_path):
    lab_map, start_pos, start_dir = parse_map(file_path)
    visited_positions = simulate_patrol(lab_map, start_pos, start_dir)
    return len(visited_positions)

# Path to the input file
file_path = "input.txt"

# Calculate the result
result = count_visited_positions(file_path)
print(f"Distinct positions visited by the guard: {result}")
