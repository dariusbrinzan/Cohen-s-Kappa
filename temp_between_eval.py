import pandas as pd
import matplotlib.pyplot as plt

# Load the evaluator data
input_file = "evaluator_data.csv"
data = pd.read_csv(input_file)

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(data['evaluator1'], data['evaluator2'], alpha=0.7, edgecolors='k')
plt.title("Scatter Plot of Evaluator Temperatures", fontsize=14)
plt.xlabel("Evaluator 1 (SME2) Temperature (°C)", fontsize=12)
plt.ylabel("Evaluator 2 (SMF1) Temperature (°C)", fontsize=12)
plt.grid(True)
plt.savefig("scatter_plot_evaluators.png")
plt.show()
