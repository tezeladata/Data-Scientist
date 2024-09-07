import pandas as pd
import numpy as np

# Pandas provides two types of classes for handling data:
# Series: a one-dimensional labeled array holding data of any type
# such as integers, strings, Python objects etc.
# DataFrame: a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns.

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
print(s.dtype)


# Creating a DataFrame by passing a NumPy array with a datetime index using date_range() and labeled columns:
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
print("\n")

# A DataFrame is an object that stores data as rows and columns. You can think of a DataFrame as a spreadsheet or as a SQL table. You can manually create a DataFrame or fill it with data from a CSV, an Excel spreadsheet, or a SQL query.
# DataFrames have rows and columns. Each column has a name, which is a string. Each row has an index, which is an integer. DataFrames can contain many different data types: strings, ints, floats, tuples, etc.
df1 = pd.DataFrame({
    "Name": ["David", "Andria", "Tobi"],
    "Address": ["1", "2", "3"]
})
print(f"\n{df1}\n")

df2 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ["t-shirt", "t-shirt", "skirt", "skirt"],
  "Color": ["blue", "green", "red", "black"]
})

print(f"\n{df2}\n")


# If we do not want to write dicts, we can give matrices
df3 = pd.DataFrame([
    ["bmw", "audi", "porsche"],
    ["Germany", "Germany", "Germany"],
    ["e34", "a7", "911"]
], columns=["Brand", "Country", "Model"])
print(f"\n{df3}\n")

df4 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, "San Francisco", 90],
  [4, "Sacramento", 115]
],
  columns=[
    "Store ID", "Location", "Number of Employees"
  ])

print(print(f"\n{df4}\n"))


# When you have data in a CSV, you can load it into a DataFrame in Pandas using .read_csv():
x = pd.read_csv("sample.csv")
print(x)

# We can also save our dataframe into csv file
df3.to_csv("new.csv")



# stopped at 6/15