import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv("housing_sample.csv")

# Scatter plot - quantitative variable plus quantitative variable
plt.scatter(x = df1.beds, y = df1.sqfeet)
plt.xlabel("Beds count")
plt.ylabel("Square feet")
plt.show()
plt.close()


# Covariance can range from negative infinity to positive infinity. A positive covariance indicates that a larger value of one variable is associated with a larger value of the other. A negative covariance indicates a larger value of one variable is associated with a smaller value of the other. A covariance of 0 indicates no linear relationship.
cov1 = np.cov(df1.beds, df1.sqfeet)
print(cov1)



# Like covariance, Pearson Correlation (often referred to simply as “correlation”) is a scaled form of covariance. It also measures the strength of a linear relationship, but ranges from -1 to +1, making it more interpretable.
# Highly associated variables with a positive linear relationship will have a correlation close to 1. Highly associated variables with a negative linear relationship will have a correlation close to -1. Variables that do not have a linear association (or a linear association with a slope of zero) will have correlations close to 0.

from scipy.stats import pearsonr
corr_price_sqfeet, p = pearsonr(df1.price, df1.sqfeet)
corr_sqfeet_beds, p2 = pearsonr(df1.sqfeet, df1.beds)
print(corr_price_sqfeet, p)
print(corr_sqfeet_beds, p2)

# Generally, a correlation larger than about .3 indicates a linear association. A correlation greater than about .6 suggestions a strong linear association.

plt.scatter(x=df1.sqfeet, y=df1.beds)
plt.show()
plt.close()