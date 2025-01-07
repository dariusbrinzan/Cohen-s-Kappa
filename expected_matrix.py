import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the expected matrix
expected_matrix_file = "expected_matrix.csv"
expected_matrix = pd.read_csv(expected_matrix_file, index_col=0)

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(expected_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, linewidths=0.5)

# Add titles and labels
plt.title("Expected Matrix Heatmap", fontsize=16)
plt.xlabel("Evaluator 2 Categories", fontsize=12)
plt.ylabel("Evaluator 1 Categories", fontsize=12)

# Save the heatmap as a PNG file
output_file = "expected_matrix_heatmap.png"
plt.savefig(output_file, bbox_inches='tight', dpi=300)

print(f"Heatmap saved as {output_file}")
plt.show()
