import pandas as pd

# Path to the Excel file
excel_file = "13_OM_50.xlsx"

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file)

# Select the desired columns
selected_columns = ['OM_Regular', 'OM_Prediction']
df_selected = df[selected_columns]

# Convert the DataFrame to a tab-separated text file
output_file = "13_OM_50.txt"
df_selected.to_csv(output_file, sep='\t', index=False)

print(f"Excel file '{excel_file}' converted to '{output_file}'.")
