import csv

# Function to mark each line with 1 or 0 based on the ending
def mark_line(line):
    if line.strip().endswith(",p"):
        return 1
    elif line.strip().endswith(",np"):
        return 0
    else:
        return None

# Open the input text file
with open('pred.txt', 'r') as file:
    lines = file.readlines()

# Create a list to hold the marked lines
marked_lines = []
for line in lines:
    mark = mark_line(line)
    if mark is not None:
        marked_lines.append((line.strip(), mark))

# Write the marked lines to a CSV file
with open('red_result.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['OM_Regular', 'OM_Prediction'])
    writer.writerows(marked_lines)
