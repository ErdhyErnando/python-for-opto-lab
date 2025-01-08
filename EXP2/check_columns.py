import pandas as pd

data = pd.read_csv("./table_4_data/20100.csv")
print("Column names in the DataFrame:")
print(data.columns)
print("\nFirst few rows of data:")
print(data.head())
