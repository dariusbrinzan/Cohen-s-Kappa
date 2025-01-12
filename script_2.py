import pandas as pd
import numpy as np

input_file = "evaluator_data.csv"
data = pd.read_csv(input_file)

bins = [-np.inf, -10, 0, 10, 20, 30, np.inf]
labels = ['< -10°C', '-10°C to 0°C', '0°C to 10°C', '10°C to 20°C', '20°C to 30°C', '> 30°C']

evaluator1_categories = pd.cut(data['evaluator1'], bins=bins, labels=labels)
evaluator2_categories = pd.cut(data['evaluator2'], bins=bins, labels=labels)

print("Evaluator 1 category distribution:")
print(evaluator1_categories.value_counts())
print("\nEvaluator 2 category distribution:")
print(evaluator2_categories.value_counts())

discretized_file = "discretized_data.csv"
pd.DataFrame({'evaluator1_categories': evaluator1_categories, 'evaluator2_categories': evaluator2_categories}).to_csv(discretized_file, index=False)

print(f"Discretized data saved to {discretized_file}")
