import pandas as pd

# Specify the path to the original Excel file
original_file_path = "/Users/rashedhasan/Desktop/UNL/Research/Object relational mapping/Step 5 - Abstraction/OM-Solution_Mapping/OM-ML_Research/Combined_datasets/14-OM-datasets/unseen/10-OM-train-4-OM-test/new_label/10-OM-space.xlsx"

# Specify the path for the new Excel file with modifications
modified_file_path = "/Users/rashedhasan/Desktop/UNL/Research/Object relational mapping/Step 5 - Abstraction/OM-Solution_Mapping/OM-ML_Research/Combined_datasets/14-OM-datasets/unseen/10-OM-train-4-OM-test/new_label/10-OM-label.xlsx"

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
