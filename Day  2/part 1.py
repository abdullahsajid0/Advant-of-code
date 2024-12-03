# Function to determine if a report is safe
def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are positive (increasing) or negative (decreasing)
    all_increasing = all(0 < diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff < 0 for diff in differences)
    
    # The report is safe if it meets one of the above conditions
    return all_increasing or all_decreasing

# Read reports from the input file
def read_reports(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip().split())) for line in file]

# Path to the input file
file_path = 'input.txt'

# Read data from the file
reports = read_reports(file_path)

# Check each report for safety and count the number of safe reports
safe_reports_count = sum(is_safe(report) for report in reports)

# Output the result
print(f"Number of safe reports: {safe_reports_count}")
