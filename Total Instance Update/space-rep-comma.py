def add_comma(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    modified_lines = [line.replace(' ', ',') for line in lines]

    with open(output_file, 'w') as file:
        file.writelines(modified_lines)

# Example usage:
input_file_path = 'text.txt'
output_file_path = 'commatext.txt'
add_comma(input_file_path, output_file_path)
