import os
import pandas as pd

# Set the directory path containing the XLSX files
directory = "/Users/admin0513-27/Documents/GitHub/OM-ML_Research/Combined_datasets/15-OM/20P-80NP/dataset/output"

# Initialize an empty DataFrame to store combined data
combined_data = pd.DataFrame()

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        # Read the XLSX file into a DataFrame
        filepath = os.path.join(directory, filename)
        df = pd.read_excel(filepath)

        # Verify if 'OM_Regular' and 'OM_Prediction' columns exist
        if 'OM_Regular' not in df.columns or 'OM_Prediction' not in df.columns:
            print(f"Warning: Missing 'OM_Regular' or 'OM_Prediction' columns in file: {filename}")
            continue

        # Append the DataFrame to the combined_data DataFrame
        combined_data = pd.concat([combined_data, df[['OM_Regular', 'OM_Prediction']]], axis=0)

# Write the combined data to an XLSX file
combined_data.to_excel("15_OM_20.xlsx", index=False)
