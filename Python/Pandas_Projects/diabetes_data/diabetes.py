# Import pandas module.
import pandas as pd

# Use pandas to read your CSV file, and initiate a DataFrame variable.
df = pd.read_csv("diabetes.csv")

# # .head() let's you glimpse the first 5 (default) rows.
# print(df.head())

# # .tail() let's you glimpse end rows; the n argument in .head() or .tail() will specify a number of rows.
# print(df.tail(n=10))

# # .describe() prints a statistics summary of all numeric columns.
# print(df.describe())

# # Modify the percentiles using the percentiles argument.
# print(df.describe(percentiles=[0.3, 0.5, 0.7]))

# # Isolate data types in the output by using the include argument.
# print(df.describe(include=[int]))

# # The exclude arguments works as well.
# print(df.describe(exclude=[int]))

# # Transpose the statistics summary with the .T attribute.
# print(df.describe().T)

# # .info() displays data types, missing values, and the data size of a DataFrame.
# print(df.info())
# print(df.info(show_counts=True, memory_usage=True, verbose=True))

# # The .shape attribute outputs the numver of rows and columns, use [0] for rows only and [1] for colimns only.
# print(df.shape)
# print(df.shape[0])
# print(df.shape[1])

# # .columns attribute returns cilumn names as an Index object. Convert to a list with the list() function.
# print(df.columns)
# print(list(df.columns))

# .copy() makes a copy of the original DataFrame.
df2 = df.copy()

# The original DataFrame does not have any missing values, we will create some using concepts described later.
df2.loc[2:5, 'Pregnancies'] = None
print(df2.head(7))

# Check for missing values using .isnull(), combine with .sum() to count the number of nulls in each column. Double .sum() will output the total nulls in the DataFrame.
print(df2.isnull().head(7))
print(df2.isnull().sum())
print(df2.isnull().sum().sum())

# Isolate a column using []


# .loc[] (location) and .iloc[] (integer location) can fetch specific rows by labels or conditions.
print(df2.loc[1])
print(df2.iloc[1])
print(df2.loc[100:110]) 