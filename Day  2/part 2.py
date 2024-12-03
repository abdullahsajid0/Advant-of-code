# Function to determine if a report is safe
def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are positive (increasing) or negative (decreasing)
    all_increasing = all(0 < diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff < 0 for diff in differences)
    
    # The report is safe if it meets one of the above conditions
    return all_increasing or all_decreasing

# Function to check if removing one level makes the report safe
def is_safe_with_dampener(report):
    # If the report is already safe, return True
    if is_safe(report):
        return True
    
    # Otherwise, check if removing any single level makes it safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    
    return False

# Read reports from the input file
def read_reports(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip().split())) for line in file]

# Path to the input file
file_path = 'input.txt'

# Read data from the file
reports = read_reports(file_path)

# Check each report for safety with the dampener and count the number of safe reports
safe_reports_count = sum(is_safe_with_dampener(report) for report in reports)

# Output the result
print(f"Number of safe reports with Problem Dampener: {safe_reports_count}")
