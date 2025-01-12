import pandas as pd

# Load the dataset
file_path = "air_temp_final.csv"  # Update the path if necessary
data = pd.read_csv(file_path)

# Select columns for the two evaluators
evaluator1 = data['sme2_ta_C']
evaluator2 = data['smf1_ta_C']

# Save the evaluator data to a CSV file
output_file = "evaluator_data.csv"
pd.DataFrame({'evaluator1': evaluator1, 'evaluator2': evaluator2}).to_csv(output_file, index=False)

print(f"Evaluator data saved to {output_file}")
