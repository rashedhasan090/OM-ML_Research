import openpyxl

def count_instances(input_file, output_file):
    # Load the Excel file
    workbook = openpyxl.load_workbook(input_file)
    sheet = workbook.active

    # Find the column index for "OM_Prediction"
    om_prediction_index = None
    for cell in sheet[1]:
        if cell.value == "OM_Prediction":
            om_prediction_index = cell.column
            break

    if om_prediction_index is None:
        print("Column 'OM_Prediction' not found in the Excel file.")
        return

    # Scan all rows in the OM_Prediction column
    om_prediction_column = sheet[om_prediction_index]
    p_count = 0
    np_count = 0

    for cell in om_prediction_column[1:]:
        value = cell.value
        if value and isinstance(value, str):
            if value.startswith('P, '):
                p_count += 1
            elif value.startswith('NP, '):
                np_count += 1

    # Write the counts to the output file
    with open(output_file, 'w') as file:
        file.write(f'Instances starting with "P, ": {p_count}\n')
        file.write(f'Instances starting with "NP, ": {np_count}\n')

    print("Counts written to the output file.")

# Provide the input file path and output file path
input_file = '15_OM_final_training_set_1.xlsx'
output_file = '15_OM_final_training_set_1.txt'

# Call the function to count instances and write the results
count_instances(input_file, output_file)


