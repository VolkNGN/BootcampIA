import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

print("First 5 rows: \n", df.head())
print("Last 5 rows: \n", df.tail())
print(df.describe())
