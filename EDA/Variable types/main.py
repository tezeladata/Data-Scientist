# Exploratory Data Analysis (EDA for short) is all about getting curious about your data – finding out what is there, what patterns you can find, and what relationships exist. EDA is the important first step towards analysis and model building. When done well, it can help you formulate further questions and areas for investigation, and it almost always helps uncover aspects of your data that you wouldn’t have seen otherwise.

# Variables define datasets. They are the characteristics or attributes that we evaluate during data collection. There are two ways to do that evaluation: we can measure or we can categorize.


import pandas as pd

df1 = pd.read_csv("netflix_movies.csv")
print(df1.head())

# The price column describes how much the cereal costs. We don’t know if that’s how much the consumer pays or the grocer pays, but we can be fairly sure that it’s a numerical variable.
# In the mfr column, there are labels like Nestle, Quaker Oats, and Kelloggs, which seem like brands. Since brands are categories, mfr is most likely a categorical variable.
# The id column also has numbers, but we can assume that since it’s the id, it’s not actually representing a value. It’s probably the label for the observation. Since it’s a label, even though it’s a number, id is a categorical variable.


# Categorical variables come in 3 types:
#
# Nominal variables, which describe something,
# Ordinal variables, which have an inherent ranking, and
# Binary variables, which have only two possible variations.


# When we want to describe something about the world, we need a nominal variable. Nominal variables are usually words (i.e., red, yellow, blue or hot, cold), but they can also be numbers (i.e., zip codes or user id’s).

# When our categories have an inherent order, we need an ordinal variable. Ordinal variables are usually described by numbers like 1st, 2nd, 3rd. Places in a race, grades in school, and the scales in survey responses (Likert Scales) are ordinal variables.
# Ordinal variables can be a little tricky because even though they are numbers, it doesn’t make sense to do math on them. For example, let’s say an Olympian won a Gold medal (1st place) and a Bronze medal (3rd place). We wouldn’t say that they averaged Silver medals (2nd place).

# When there are only two logically possible variations, we need a binary variable. Binary variables are things like on/off, yes/no, and TRUE/FALSE. If there is any possibility of a third option, it is not a binary variable.


# Continuous variables come from measurements. For a variable to be continuous, there must be infinitely smaller units of measurement between one unit and the next unit. Continuous variables can be represented by decimal places (but because of rounding, sometimes they are whole numbers). Length, time, and temperature are all good examples of continuous variables because they all increase continuously.

# Discrete variables come from counting. For a variable to be discrete, there must be gaps between the smallest possible units. People, cars, and dogs are all good examples of discrete variables.


# With numerical variables, pandas expects any column that has decimal values to be a float and anything without decimal values to be an integer. If any non-numeric characters appear in the column, pandas will treat it as an object.


# Best practices for data storage say that we should match the data type of the column with its real-world variable type. Therefore:
# Continuous (numerical) variables should usually be stored as the float data type because they allow us to store decimal values.
# Discrete (numerical) variables should be stored as the int datatype to represent mathematically that they are discrete.


# We can use .dtypes method to see data types of all items
print(df1.dtypes)


# If a variable appears with the wrong data type, we can change it with the .astype() function.
df1["duration"] = df1["duration"].round().astype("Int64")
print(df1)

# The .astype() function can be used to convert between a numerical data types, including:
# int32 int64
# float32 float64
# object
# string
# bool


# Just like with numerical variables, best practices for categorical data storage say that we should match the data type of the column with its real-world variable type. However, the types are a little more nuanced:

# Nominal variables are often represented by the object data type. Columns in the object data type can contain any combination of values, including strings, integers, booleans, etc. This means that string operations like .lower() are not possible on object columns.
# Nominal variables are also represented by the string data type. However, Pandas usually guesses object rather than string, so if you want a column to be a string, you will likely have to explicitly tell pandas to make it a string. This is most important if you want to do string manipulations on a column like .lower().
# Ordinal variables should be represented as objects, but pandas often guesses int since they are often encoded as whole numbers.
# Binary variables can be represented as bool, but pandas often guesses int or object data types.


# there is a specific data type for categorical variables in pandas called category to address this problem! The pandas .Categorical() method can be used to store data as type category and indicate the order of the categories.
# cereal['shelf'] = pd.Categorical(cereal['shelf'], ['bottom', 'mid', 'top'], ordered=True)

df1["rating"] = pd.Categorical(df1["rating"], ["NR", "G", "PG", "PG-13", "R"], ordered=True)




census = pd.read_csv('census_data.csv', index_col=0)
print(census.head())
print(census.dtypes)

census['birth_year'] = census['birth_year'].replace(['missing'], "1967")
print(census['birth_year'].unique())

census['birth_year'] = census['birth_year'].astype("int64")
print(census['birth_year'].unique())

print(census['birth_year'].mean())

census["higher_tax"] = pd.Categorical(census["higher_tax"], ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"], ordered=True)
print(census["higher_tax"].unique())

census['higher_tax'] = census['higher_tax'].cat.codes
print(census['higher_tax'].median())

census = pd.get_dummies(census, columns=['marital_status'])
print(census.head())