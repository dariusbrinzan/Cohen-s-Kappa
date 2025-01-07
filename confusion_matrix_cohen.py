import pandas as pd
from sklearn.metrics import cohen_kappa_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load discretized data
discretized_file = "discretized_data.csv"
data = pd.read_csv(discretized_file)

# Build confusion matrix
confusion_matrix = pd.crosstab(data['evaluator1_categories'], data['evaluator2_categories'])

# Display and save confusion matrix
print("Confusion Matrix:")
print(confusion_matrix)
confusion_matrix.to_csv("confusion_matrix.csv")

# Calculate Cohen's Kappa
kappa_score = cohen_kappa_score(data['evaluator1_categories'], data['evaluator2_categories'])
print(f"\nCohen's Kappa Score: {kappa_score:.3f}")

# Visualize confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix (Evaluator 1 vs Evaluator 2)")
plt.xlabel("Evaluator 2 Categories")
plt.ylabel("Evaluator 1 Categories")
plt.savefig("confusion_matrix_heatmap.png")
plt.show()
