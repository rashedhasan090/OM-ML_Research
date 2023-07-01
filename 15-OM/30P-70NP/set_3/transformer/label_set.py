import csv

def generate_csv(input_file, output_file):
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["OM_regular", "OM_Prediction"])

        with open(input_file, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("[start] assoc5assocstr2"):
                    writer.writerow([line, 0])
                else:
                    writer.writerow([line, 1])

    print(f"Generated {output_file} successfully.")

# Usage example
input_file = "pred.txt"
output_file = "random_set_3.0-prd.csv"
generate_csv(input_file, output_file)

