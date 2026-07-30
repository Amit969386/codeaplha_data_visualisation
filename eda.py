import pandas as pd

# Load Dataset
df = pd.read_csv("titanic.csv")

# First 5 Rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Statistical Summary
print("\nSummary:")
print(df.describe())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())