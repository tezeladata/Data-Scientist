# it’s time to explore some numeric variables — those with quantitative data
# There are a lot of ways we can describe the distribution of a numeric variable. A distribution is a function that shows all possible values of a variable and how frequently each value occurs. This may sound pretty technical, but visualizing the distribution can make it easy to understand.

# This distribution might be considered bell-shaped or hill-shaped and symmetrical. This is actually a very common pattern and is called a normal distribution.

# The mean, also called the average, describes the center of a numeric distribution by adding all values and dividing by the count.
# The standard deviation describes the spread of values in a numeric distribution relative to the mean. It is calculated by finding the average squared distance from each data point to the mean and square-rooting the result.

# The mean and standard deviation are common choices, especially for normal distributions. Their mathematical formulas have special properties that make them easy to use in other contexts, such as statistical testing. However, the mean and standard deviation are not always the best measurements to describe a distribution.

# What we have learned is that the income distribution is skewed. A skewed distribution is asymmetrical with a steep change in frequency on one side and a flatter, trailing change in frequency on the other. Specifically, the income distribution is right-skewed (also called positively-skewed) because the tail is on the right side.


# One method to find average value would be to find the middle value when all values are arranged from smallest to largest. This value is called the median, but it’s also referred to as the 50th percentile or the second quartile (Q2).

# These data span 22 values, ranging from 6 to 28. We could use this as our measure of spread, but what if the highest number wasn’t 28 but 280? The median would still be 13, but now the range is 274 (280-6), which doesn’t tell us a lot about the bulk of the data.
# A better measurement might be the interquartile range (IQR). A quartile is simply a marker for a quarter (25%) of the data.
# The first quartile marks 25% (Q1 = 10).
# The second quartile marks 50% (Q2 = 13 — the median)
# The third quartile marks 75% (Q3 = 22)
# And when we count iqr: q3-q1 = 17150

# These celebrity incomes are examples of outliers, extreme values that are distant from the rest of the distribution. Just as with skewness, outliers tend to more heavily influence the mean than the median. This same pattern occurs with measures of spread: the standard deviation is more influenced by outliers and skewness than the interquartile range (IQR).


# Because the median and IQR are NOT heavily influenced by extreme values, we say they are robust. Robust statistics are often a better choice to measure the center and spread of a distribution that is skewed or has outliers.

# One measure that we haven’t covered that is usually talked about alongside the mean and median is the mode. The mode is defined as the value with the highest frequency, but we can also think of the mode as the value where the peak of the distribution occurs. While not great for computations, the mode can help us identify interesting features in a variable.

# In the following plot, we can see there’s one peak near the 10-year mark and another near the 30-year mark. We would call this distribution bimodal because it has two modes.

# Aggregating data is a way of exploring variable relationships. We specifically looked at relationships between a numeric variable and a categorical variable, but we should also examine relationships between two numeric variables.


# The cloud of points in the plot has a pattern. The points move from the lower left to the upper right part of the plot. In other words, lower levels of experience tend to be associated with lower incomes, and higher levels of experience tend to be associated with higher incomes. The points don’t form a perfect line though — there is some variation.