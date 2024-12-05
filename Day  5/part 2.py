from collections import defaultdict, deque

def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().strip().split('\n')
    
    # Split rules and updates
    split_index = lines.index("")
    rules = lines[:split_index]
    updates = lines[split_index + 1:]
    
    # Parse rules
    parsed_rules = []
    for rule in rules:
        x, y = map(int, rule.split('|'))
        parsed_rules.append((x, y))
    
    # Parse updates
    parsed_updates = []
    for update in updates:
        parsed_updates.append(list(map(int, update.split(','))))
    
    return parsed_rules, parsed_updates

def is_update_ordered(update, rules):
    # Create a dictionary to store the index of each page in the update
    page_index = {page: idx for idx, page in enumerate(update)}
    
    for x, y in rules:
        # Only check rules where both X and Y are in the update
        if x in page_index and y in page_index:
            if page_index[x] >= page_index[y]:  # X must come before Y
                return False
    return True

def fix_order(update, rules):
    # Build a graph from the rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Only consider rules relevant to this update
    update_set = set(update)
    for x, y in rules:
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree[x] += 0  # Ensure all nodes exist in the in_degree map

    # Topological sort to find the correct order
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_pages = []
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages

def calculate_fixed_middle_sum(file_path):
    # Parse input
    rules, updates = parse_input(file_path)
    total = 0

    for update in updates:
        # Check if the update is correctly ordered
        if not is_update_ordered(update, rules):
            # Fix the order of the update
            fixed_update = fix_order(update, rules)
            # Find the middle page number
            mid_page = fixed_update[len(fixed_update) // 2]
            total += mid_page
    
    return total

# Path to the input file
file_path = "input.txt"

# Calculate the result for Part Two
result = calculate_fixed_middle_sum(file_path)
print(f"The sum of middle page numbers of fixed updates is: {result}")
