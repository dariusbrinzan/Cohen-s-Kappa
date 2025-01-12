import pandas as pd
import numpy as np

def cochran_sample_size(N=None, Z=1.96, p=0.5, e=0.05):
    """
    Calculate sample size using Cochran's formula.
    
    Parameters:
    - N: Total population size (None for infinite population).
    - Z: Z-score for the desired confidence level (default: 1.96 for 95% confidence).
    - p: Estimated proportion of the population (default: 0.5 for maximum variability).
    - e: Desired margin of error (default: 0.05 for 5% margin).
    
    Returns:
    - n: Required sample size.
    """
    n0 = (Z**2 * p * (1 - p)) / (e**2)
    
    if N is not None:
        n = n0 / (1 + (n0 - 1) / N)
    else:
        n = n0
    
    return round(n)

def extract_sample(dataset, sample_size):
    """
    Extract a random sample from the dataset.
    
    Parameters:
    - dataset: Pandas DataFrame containing the population data.
    - sample_size: Size of the sample to extract.
    
    Returns:
    - sample: A Pandas DataFrame containing the extracted sample.
    """
    return dataset.sample(n=sample_size, random_state=42)

file_path = "air_temp_final.csv"
data = pd.read_csv(file_path)

population_size = len(data)
confidence_level = 0.95
margin_of_error = 0.05
proportion = 0.5

sample_size = cochran_sample_size(N=population_size, Z=1.96, p=proportion, e=margin_of_error)
print(f"Required sample size: {sample_size}")

sample = extract_sample(data, sample_size)

sample_file = "sampled_data.csv"
sample.to_csv(sample_file, index=False)
print(f"Sample saved to {sample_file}")
