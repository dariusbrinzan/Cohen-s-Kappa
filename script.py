import pandas as pd

file_path = "air_temp_final.csv"
data = pd.read_csv(file_path)

evaluator1 = data['sme2_ta_C']
evaluator2 = data['smf1_ta_C']

output_file = "evaluator_data.csv"
pd.DataFrame({'evaluator1': evaluator1, 'evaluator2': evaluator2}).to_csv(output_file, index=False)

print(f"Evaluator data saved to {output_file}")
