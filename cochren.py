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
    # Step 1: Calculate the initial sample size (n0)
    n0 = (Z**2 * p * (1 - p)) / (e**2)
    
    # Step 2: Adjust for finite population (if N is provided)
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

# Step 1: Load your dataset
file_path = "air_temp_final.csv"  # Update with your dataset path
data = pd.read_csv(file_path)

# Step 2: Calculate the required sample size
population_size = len(data)  # Total population size
confidence_level = 0.95      # 95% confidence level
margin_of_error = 0.05       # 5% margin of error
proportion = 0.5             # Assume 50% for maximum variability

sample_size = cochran_sample_size(N=population_size, Z=1.96, p=proportion, e=margin_of_error)
print(f"Required sample size: {sample_size}")

# Step 3: Extract the sample
sample = extract_sample(data, sample_size)

# Step 4: Save the sample to a CSV file
sample_file = "sampled_data.csv"
sample.to_csv(sample_file, index=False)
print(f"Sample saved to {sample_file}")
