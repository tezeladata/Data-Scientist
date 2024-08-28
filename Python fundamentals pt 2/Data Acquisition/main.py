# importing requests library for API
import requests

# Next, we will use get method to get data from URL
r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*')

# This is response object
print(r)

# We can turn this into text, using .text method
print(r.text)

# If we want to have data in better structure, we can use .json method
print(r.json())

r2 = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')
print(r2.json())
print(type(r2))


# Csv for tabular information
import csv


# The JSON data we got from the Census API is a list of lists in Python, where each inner list corresponds to a single row of data. To convert from JSON to CSV, we want to write each sublist as a comma-separated row of data to file.

with open('census.csv', mode='w', newline='\n') as file:
    writer = csv.writer(file)
    writer.writerow(r.json())

# open - open file
# as file - create variable called file
# we are going to write that file s0 - mode="w"
# newline="" - newlines are separated
# writer - writer object
# writerows - comma-separated format for each row



# Now we want to work with csv file easily, so we use pandas
import pandas

census_df = pandas.read_csv('census.csv')
# df stands for dataframe object

# By default, the first row of the CSV file is read in as the header row. We can use the .head() method to preview the first few rows of the DataFrame.

# census_df.columns = ["a", "b", "c"]

# Preview dataframe
print(census_df.head())



# Binomial events always have 2 possible outcomes, which we refer to as success and failure. The probability of a successful outcome is represented by the parameter p. For example, for the event of a coin toss using a fair coin, p would be 0.5.
# There are lots of ways to do this. We could flip a coin a bunch of times and write down the results or we could use the random.binomial() method from the numpy library in Python.
# To use the random.binomial() method, we have to tell it how many trials we want to simulate (n) and the probability of ‘success’ in a single trial (p), and how many experiments to run.
# In the example below, there was 1 flip per trial (n), the probability (p) of getting ‘success’ was .5 (the coin is fair), and we conducted the experiment 2,000 times (size).

import numpy

print(numpy.random.binomial(n=100, p=0.8, size=500))