# Lab 1: Introduction to Pandas
import pandas as pd

# Creating a Series
series = pd.Series([10, 20, 30, 40, 50])
print(series)

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)


# Lab 2: Pandas Data Structures
# Creating Series from a dictionary
series = pd.Series({'a': 100, 'b': 200, 'c': 300})
print(series)

# Creating DataFrame from a list of lists
df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
print(df)

# Converting Series to DataFrame
df_from_series = series.to_frame()
print(df_from_series)


# Lab 3: Handling Missing Data
import numpy as np

df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
print(df.isnull())

df_filled = df.fillna(0)
print(df_filled)

df_dropped = df.dropna()
print(df_dropped)


# Lab 4: Renaming Columns and Rows
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df.rename(columns={'col1': 'Column1', 'col2': 'Column2'}, inplace=True)
df.rename(index={0: 'First', 1: 'Second'}, inplace=True)
print(df)


# Lab 5: Data Transformation with apply(), map(), applymap()
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Apply function to each column
df['A'] = df['A'].apply(lambda x: x * 2)

# Map function to a Series
df['B'] = df['B'].map(lambda x: x + 10)

# Applymap for element-wise operation
df = df.applymap(lambda x: x ** 2)

print(df)


# Lab 6: String Manipulation with str
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']})
df['Uppercase'] = df['Name'].str.upper()
df['First3'] = df['Name'].str[:3]
print(df)


# Lab 7: Grouping Data with groupby()
df = pd.DataFrame({'Category': ['A', 'B', 'A', 'B'], 'Value': [10, 20, 30, 40]})
grouped = df.groupby('Category').mean()
print(grouped)


# Lab 8: Data Aggregation
df = pd.DataFrame({'Category': ['X', 'Y', 'X', 'Y'], 'Values': [10, 20, 30, 40]})
print(df.groupby('Category').sum())
print(df.groupby('Category').agg(['sum', 'mean']))


# Lab 9: Sorting and Ranking
df = pd.DataFrame({'A': [3, 1, 2], 'B': [6, 5, 4]})
df_sorted = df.sort_values(by='A')
df['Rank'] = df['A'].rank()
print(df_sorted)
print(df)


# Lab 10: Merge and Join
df1 = pd.DataFrame({'ID': [1, 2], 'Value': ['A', 'B']})
df2 = pd.DataFrame({'ID': [1, 2], 'Score': [90, 80]})
merged_df = pd.merge(df1, df2, on='ID')
print(merged_df)


# Lab 11: Reshaping and Pivot Tables
df = pd.DataFrame({'ID': [1, 2], 'Year': [2020, 2021], 'Score': [88, 92]})
df_pivot = df.pivot(index='ID', columns='Year', values='Score')
df_melt = pd.melt(df, id_vars=['ID'], var_name='Attribute', value_name='Value')
print(df_pivot)
print(df_melt)


# Lab 12: Handling Time Series
df = pd.DataFrame({'Date': ['2022-01-01', '2023-01-02']})
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
print(df)


# Lab 13: Data Visualization with Pandas
import matplotlib.pyplot as plt

df = pd.DataFrame({'Year': [2018, 2019, 2020, 2021], 'Sales': [100, 200, 150, 300]})

df.plot(x='Year', y='Sales', kind='line', marker='o', title='Sales Over Years')
plt.show()

df.plot(x='Year', y='Sales', kind='bar', title='Sales Per Year')
plt.show()


# Lab 14: Creating Pivot Tables
df = pd.DataFrame({'Region': ['East', 'West', 'East', 'West', 'East'],
                   'Salesperson': ['Alice', 'Bob', 'Charlie', 'Alice', 'Charlie'],
                   'Sales': [200, 150, 300, 400, 250]})

pivot_df = df.pivot_table(values='Sales', index='Region', columns='Salesperson', aggfunc='sum', fill_value=0)
print(pivot_df)


# Lab 15: One-Hot Encoding with get_dummies()
df = pd.DataFrame({'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']})
df_encoded = pd.get_dummies(df, columns=['City'])
print(df_encoded)


# Lab 16: Cross-Tabulation using crosstab()
df = pd.DataFrame({'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
                   'Product': ['A', 'A', 'B', 'B', 'A']})

crosstab_result = pd.crosstab(df['Gender'], df['Product'])
print(crosstab_result)


# Lab 17: Splitting Data into Bins with cut()
ages = pd.DataFrame({'Age': [10, 25, 40, 55, 70, 85]})
bins = [0, 18, 35, 50, 65, 100]
labels = ['Child', 'Young Adult', 'Adult', 'Middle-aged', 'Senior']
ages['Age Group'] = pd.cut(ages['Age'], bins=bins, labels=labels)
print(ages)


# Lab 18: Factorizing Categorical Variables
df = pd.DataFrame({'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']})
df['Department_Code'], mapping = pd.factorize(df['Department'])
print(df)
print("Mapping:", mapping)


# Lab 19: Exploding Lists in a DataFrame
df = pd.DataFrame({'Employee': ['Alice', 'Bob'], 'Skills': [['Python', 'SQL'], ['Excel', 'PowerPoint']]})
df_exploded = df.explode('Skills')
print(df_exploded)


