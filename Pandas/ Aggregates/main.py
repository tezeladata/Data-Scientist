# An aggregate statistic is a way of creating a single number that describes a group of numbers. Common aggregate statistics include mean, median, and standard deviation.
import numpy as np
# General syntax for pandas aggregates is:
# df.column_name.command()
# mean	Average of all values in column
# std	Standard deviation
# median	Median
# max	Maximum value in column
# min	Minimum value in column
# count	Number of values in column
# nunique	Number of unique values in column
# unique	List of unique values in column

import pandas as pd

df1 = pd.read_csv('orders.csv')
print(df1.head(10))
print(f"The most expensive shoe costs {df1.price.max()}")
print(f"The least expensive shoe costs {df1.price.min()}")
print(f"There are {df1.shoe_material.nunique()} different shoe materials")
print(f"There are {df1.shoe_color.nunique()} different shoe colors")
print("\n\n")

# When we have columns, which have same person or something related to repeating, we can use groupby to calculate e.g mean of person's score
df2 = pd.DataFrame([
    ["Amy", "Assignment 1", 75],
    ["Amy", "Assignment 2", 35],
    ["Bob", "Assignment 1", 99],
    ["Bob", "Assignment 2", 35]
], columns=["student", "assignment_name", "grade"])
print(df2)
print(df2.groupby("student").grade.mean())

# General syntax for groupby:
# df.groupby('column1').column2.measurement()
# column1 is the column that we want to group by ('student' in our example)
# column2 is the column that we want to perform a measurement on (grade in our example)
# measurement is the measurement function we want to apply (mean in our example)

print(f"\nAverage score for each assignment is: {df2.groupby('assignment_name').grade.mean()}")

# other example:
print(f"Most expensive shoe for each type is \n{df1.groupby('shoe_type').price.max()}")
# When new series are created after using groupby, indices are not sorted, so we can use reset_index


# When we have more complex scenario, we can use percentile method:
df3  = pd.DataFrame([
    ["Sarah Carney", 39, "design"],
    ["Heather Carey", 17, "design"],
    ["Gary Mercado", 33, "design"],
    ["Cora Cops", 27, "design"]
], columns=["name", "wage", "category"])
print(df3.groupby("category").wage.apply(lambda x: np.percentile(x, 60)))
# Point, where 60% of wages are lower and 40% of wages are higher


# Sometimes we want to combine columns and use groupby method
df4 = pd.DataFrame([
    ["West Village", "February 1", "W", 400],
    ["West Village", "February 2", "W", 700],
    ["Chelsea", "February 1", "M", 100],
    ["Chelsea", "February 2", "M", 300],
], columns=["Location", "Date", "Day of Week", "Total Sales"])
print(df4.groupby(["Location", "Day of Week"])["Total Sales"].mean())


# When we want to rearange DataFrame into more vertical or horizontal form, it's called pivoting
# df.pivot(columns='ColumnToPivot',
#          index='ColumnToBeRows',
#          values='ColumnToBeValues')


# Example of pivot:
shoe_counts = df1.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
shoe_counts_pivot = shoe_counts.pivot(columns="shoe_color", index="shoe_type", values="id").reset_index()
print(shoe_counts_pivot)