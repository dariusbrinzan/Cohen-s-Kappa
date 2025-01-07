import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the categories
categories = ['< -10°C', '-10°C to 0°C', '0°C to 10°C', '10°C to 20°C', '20°C to 30°C', '> 30°C']
num_categories = len(categories)

# Calculate the weight matrix with high precision
weights = np.zeros((num_categories, num_categories))
for i in range(num_categories):
    for j in range(num_categories):
        weights[i, j] = 1 - abs(i - j) / (num_categories - 1)

# Convert to a DataFrame for better readability
weight_matrix = pd.DataFrame(weights, index=categories, columns=categories)

# Save the weight matrix
weight_matrix_file = "weight_matrix.csv"
weight_matrix.to_csv(weight_matrix_file)

# Display the weight matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(weight_matrix, annot=True, fmt=".3f", cmap="coolwarm", cbar=True, linewidths=0.5)

# Add titles and labels
plt.title("Weight Matrix Heatmap", fontsize=16)
plt.xlabel("Evaluator 2 Categories", fontsize=12)
plt.ylabel("Evaluator 1 Categories", fontsize=12)

# Save the heatmap as a PNG file
output_file = "weight_matrix_heatmap.png"
plt.savefig(output_file, bbox_inches='tight', dpi=300)

print(f"Weight matrix saved to {weight_matrix_file}")
print(f"Heatmap saved to {output_file}")
plt.show()
