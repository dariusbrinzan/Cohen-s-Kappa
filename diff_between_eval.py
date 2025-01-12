import pandas as pd
import matplotlib.pyplot as plt

input_file = "evaluator_data.csv"
data = pd.read_csv(input_file)

data['difference'] = data['evaluator1'] - data['evaluator2']

plt.figure(figsize=(8, 6))
plt.boxplot(data['difference'], vert=False, patch_artist=True, 
            boxprops=dict(facecolor="lightblue", color="blue"),
            medianprops=dict(color="red"), whiskerprops=dict(color="blue"))
plt.title("Box Plot of Differences Between Evaluators", fontsize=14)
plt.xlabel("Difference (Evaluator 1 - Evaluator 2) (°C)", fontsize=12)
plt.grid(axis='x')
plt.savefig("box_plot_differences.png")
plt.show()
