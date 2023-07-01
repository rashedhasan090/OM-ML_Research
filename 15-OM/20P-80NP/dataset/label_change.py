import os
import pandas as pd

# Get the current directory
current_directory = os.getcwd()

# Create a new folder named "output" if it doesn't exist
output_folder = os.path.join(current_directory, "output")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of all .xlsx files in the current directory
xlsx_files = [file for file in os.listdir(current_directory) if file.endswith(".xlsx")]

# Iterate over each .xlsx file
for file in xlsx_files:
    # Specify the path to the original Excel file
    original_file_path = os.path.join(current_directory, file)

    # Specify the path for the new Excel file with modifications
    modified_file_path = os.path.join(output_folder, file)

    # Load the original Excel file into a DataFrame
    df = pd.read_excel(original_file_path)

    # Iterate over each row in the "OM_Prediction" column
    for index, row in df.iterrows():
        prediction = str(row["OM_Prediction"])  # Assuming the column name is "OM_Prediction"

        # Check if the prediction ends with ",P" and modify accordingly
        if prediction.endswith(",P"):
            prediction = "P, " + prediction[:-2]
        # Check if the prediction ends with ",NP" and modify accordingly
        elif prediction.endswith(",NP"):
            prediction = "NP, " + prediction[:-3]

        # Update the corresponding row in the DataFrame
        df.at[index, "OM_Prediction"] = prediction

    # Save the modified DataFrame to the new Excel file
    df.to_excel(modified_file_path, index=False)