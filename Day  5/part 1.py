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

def calculate_middle_sum(file_path):
    # Parse input
    rules, updates = parse_input(file_path)
    total = 0

    for update in updates:
        # Check if the update is correctly ordered
        if is_update_ordered(update, rules):
            # Find the middle page number
            mid_page = update[len(update) // 2]
            total += mid_page
    
    return total

# Path to the input file
file_path = "input.txt"

# Calculate the result
result = calculate_middle_sum(file_path)
print(f"The sum of middle page numbers of correctly-ordered updates is: {result}")
