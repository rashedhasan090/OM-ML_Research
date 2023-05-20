def process_text_file(file_path):
    output_lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespace

            if line.endswith(',P'):
                line = 'P,' + line
            elif line.endswith(',NP'):
                line = 'NP,' + line

            output_lines.append(line)

    return output_lines


# Usage example
input_file = 'store_mgmt_labels.txt'  # Replace with the path to your input file
output_lines = process_text_file(input_file)

# Print the modified lines
for line in output_lines:
    print(line)
