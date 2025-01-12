import pandas as pd
from sklearn.metrics import cohen_kappa_score
import numpy as np
from scipy.stats import norm

data = pd.read_csv('discretized_data.csv')

print("Coloanele disponibile în fișier:", data.columns.tolist())

evaluator1 = data.iloc[:, 0]
evaluator2 = data.iloc[:, 1]

kappa = cohen_kappa_score(evaluator1, evaluator2)

conf_matrix = pd.crosstab(evaluator1, evaluator2)
total = conf_matrix.to_numpy().sum()
P_o = np.trace(conf_matrix.to_numpy()) / total
P_e = ((conf_matrix.sum(axis=0) * conf_matrix.sum(axis=1)).sum()) / (total ** 2)

SE_kappa = np.sqrt((P_o * (1 - P_o)) / (total * (1 - P_e) ** 2))

Z = norm.ppf(0.975)

lower_bound = kappa - Z * SE_kappa
upper_bound = kappa + Z * SE_kappa

print(f"Coeficientul Cohen's Kappa: {kappa:.4f}")
print(f"Intervalul de încredere 95%: ({lower_bound:.4f}, {upper_bound:.4f})")
