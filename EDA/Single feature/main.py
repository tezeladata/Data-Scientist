import pandas as pd

#This lesson focuses on univariate summaries, where we explore each variable separately. This is useful for answering questions about each individual feature. Variables can typically be classified as quantitative (i.e., numeric) or categorical (i.e., discrete). Depending on its type, we may want to choose different summary metrics and visuals to use.

df1 = pd.read_csv("movies.csv")

# Easy method for summary description
# Description without categorical columns
print(df1.describe())
# Description including categorical columns
print(df1.describe(include="all"))


# For quantitative variables, we can use following methods:
# Mean: The average value of the variable, calculated as the sum of all values divided by the number of values.
# Median: The middle value of the variable when sorted.
# Mode: The most frequent value of the variable.
# Trimmed mean: The mean excluding x percent of the lowest and highest data points.

print(df1.production_budget.mean())
print(df1.domestic_gross.median())
print(df1.worldwide_gross.mode())


# The spread of a quantitative variable describes the amount of variability. This is important because it provides context for measures of central tendency. For example, if there is a lot of variability in New York City rent prices, we can be less certain that the mean or median price is representative of what the typical rent is.
# Range: The difference between the maximum and minimum values of a variable.
# Interquartile range (IQR): The difference between the 75th and 25th percentile values.
# Variance: The average of the squared distance from each data point to the mean.
# Standard deviation (SD): The square root of the variance.
# Mean absolute deviation (MAD): The mean absolute value of the distance between each data point and the mean.


# Save the range to range_budget
range_budget = df1.production_budget.max() - df1.production_budget.min()
print(range_budget)
# Save the interquartile range to iqr_budget
iqr_budget = df1.production_budget.quantile(0.75) - df1.production_budget.quantile(0.25)
print(iqr_budget)
# Save the variance to var_budget
var_budget = df1.production_budget.var()
print(var_budget)
# Save the standard deviation to std_budget
std_budget = df1.production_budget.std()
print(std_budget)



# For quantitative variables, boxplots and histograms are two common visualizations. These plots are useful because they simultaneously communicate information about minimum and maximum values, central location, and spread. Histograms can additionally illuminate patterns that can impact an analysis (e.g., skew or multimodality).

import matplotlib.pyplot as plt
import seaborn as sns

# Boxplot
sns.boxplot(x="production_budget", data=df1)
plt.show()
plt.close()

# histogram
sns.histplot(x="production_budget", data=df1)
plt.show()
plt.close()


# The pandas library offers the .value_counts() method for generating the counts of all values in a DataFrame column
print(df1.genre.value_counts())

# Seeing proportions
print(df1.genre.value_counts() / len(df1.genre)) # Manual way
print(df1.genre.value_counts(normalize=True)) # Using method


# We can use bar charts and pie charts for good visualization about categorical variables
# Bar:
sns.countplot(x="genre", data=df1)
plt.show()
plt.close()

# pie
df1.genre.value_counts().plot.pie()
plt.show()
plt.close()