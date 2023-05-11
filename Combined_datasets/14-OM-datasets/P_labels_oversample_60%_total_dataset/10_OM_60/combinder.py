import os
import pandas as pd

# Set the directory path containing the XLSX files
directory = "/Users/rashedhasan/Desktop/UNL/Research/Object relational mapping/Step 5 - Abstraction/OM-Solution_Mapping/OM-ML_Research/Combined_datasets/13-OM-datasets/P_labels_oversample_60%_total_dataset/10_OM_60"

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
combined_data.to_excel("10_OM_60.xlsx", index=False)
