import pandas as pd

df1 = pd.read_csv('npi_sample.csv')
print(df1.head())

# Contingency tables, also known as two-way tables or cross-tabulations, are useful for summarizing two variables at the same time. For example, suppose we are interested in understanding whether there is an association between influence (whether a person thinks they have a talent for influencing people) and leader (whether they see themself as a leader). We can use the crosstab function from pandas to create a contingency table:
influence_leader_freq = pd.crosstab(df1.influence, df1.leader)
print(influence_leader_freq)

# Sometimes we want to see proportions instead of numbers:
influence_leader_prop = influence_leader_freq/len(df1)
print(influence_leader_prop)

# The proportion of respondents in each category of a single question is called a marginal proportion. For example, the marginal proportion of the population that has a talent for influencing people is 0.612.
leader_marginal = influence_leader_prop.sum(axis=0)
influence_marginal = influence_leader_prop.sum(axis=1)

print(leader_marginal)
print(influence_marginal)