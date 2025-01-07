import pandas as pd
import numpy as np

# Load matrices
confusion_matrix_file = "confusion_matrix.csv"  # Observed matrix
expected_matrix_file = "expected_matrix.csv"    # Expected matrix
weight_matrix_file = "weight_matrix.csv"        # Weight matrix

confusion_matrix = pd.read_csv(confusion_matrix_file, index_col=0).values
expected_matrix = pd.read_csv(expected_matrix_file, index_col=0).values
weight_matrix = pd.read_csv(weight_matrix_file, index_col=0).values

# Ensure the matrices have the same shape
assert confusion_matrix.shape == expected_matrix.shape == weight_matrix.shape, "Matrices must have the same dimensions."

# Calculate the numerator (weighted observed agreements)
numerator = np.sum(weight_matrix * confusion_matrix)

# Calculate the denominator (weighted expected agreements)
denominator = np.sum(weight_matrix * expected_matrix)

# Weighted Cohen's Kappa formula
weighted_kappa = 1 - (numerator / denominator)

# Display results
print(f"Numerator (Weighted Observed Agreements): {numerator:.3f}")
print(f"Denominator (Weighted Expected Agreements): {denominator:.3f}")
print(f"Cohen's Weighted Kappa: {weighted_kappa:.3f}")
