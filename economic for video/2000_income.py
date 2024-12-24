import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import numpy for median calculation

# get dataset
dataset = pd.read_csv('world_tourism_economy_data.csv')

# year == 2000 and income is not NaN
filtered_data = dataset.loc[(dataset["year"] == 2000) & (pd.notna(dataset["tourism_receipts"]))]

# Income for the year 2000
income_2000 = filtered_data["tourism_receipts"].tolist()

# Related countries
countries_2000 = filtered_data["country"].tolist()

# filter countries
def filter_countries(countries, incomes):
    # Combine countries and incomes, then sort by income
    combined = list(zip(countries, incomes))
    combined_sorted = sorted(combined, key=lambda x: x[1])

    # Median calculation
    incomes_sorted = [i[1] for i in combined_sorted]
    middle = np.median(incomes_sorted)

    # Calculate left and right boundaries
    left = middle / 2
    right = middle * 1.5

    # Dividing incomes into four groups
    lower = [i[0] for i in combined_sorted if i[1] < left]
    middle_left = [i[0] for i in combined_sorted if left <= i[1] < middle]
    middle_right = [i[0] for i in combined_sorted if middle <= i[1] < right]
    upper = [i[0] for i in combined_sorted if i[1] >= right]

    res = {
        "Lower Income": len(lower),
        "Middle left Income": len(middle_left),
        "middle right Income": len(middle_right),
        "Upper Income": len(upper)
    }

    return res

# filtering result
filter_res = filter_countries(countries_2000, income_2000)

# visualization function
def plot_dataset(fortitle, xrow_data, yrow_data):
    plt.figure(figsize=(12, 8))
    plt.bar(xrow_data, yrow_data, color="darkgreen", edgecolor="black")
    plt.ylabel("Country count", fontsize=14)
    plt.xlabel("Income groups", fontsize=14)
    plt.title(fortitle, fontsize=20)
    plt.grid(axis="y", linestyle="--", alpha=1)
    plt.tight_layout()
    plt.show()

# Call the function with updated parameters
plot_dataset("Number of countries in four groups by their tourist income", [i for i in filter_res.keys()], filter_res.values())