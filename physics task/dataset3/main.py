import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Source
# Laboratory of Meteorology, Department of Physics, University of Ioannina, GR-45110, Ioannina, Greece
# Environmental Department, Municipality of Thessaloniki, Paparigopoulou 7, Thessaloniki 54630, Greece

# read csv file
a = pd.read_csv('dataset3.csv', delimiter=',', skipinitialspace=True)

# dict for info storing
data_dict = {f"{i}:00": [] for i in range(24)}

# Iterate over rows
for index, row in a.iterrows():
    time = row["Date & Hour (EET)"].split(" ")[1]
    sound = row["Leq (dB(A)"]

    # add decibel to specific time
    data_dict[f"{time}"].append(sound)

# Final step
time, decibel = [i for i in data_dict.keys()], [sum(i) / len(i) for i in data_dict.values()]


# Convert `time` to numerical values for regression (e.g., "0:00" -> 0, ..., "23:00" -> 23)
time_numeric = list(range(24))
# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(time_numeric, decibel)
# Generate regression line
regression_line = [slope * x + intercept for x in time_numeric]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(time, decibel, marker='o', linestyle='-', color='b', label='საშუალო დეციბელი')
plt.plot(time, regression_line, color='r', linestyle='--', label=f'რეგრესიის ხაზი')

# Customize the plot
plt.title("საშუალო დეციბელის დონე 24 საათის განმავლობაში თესალონიკში - საშუალო გამოთვლილია 365 დღის მონაცემით", fontsize=10)
plt.xlabel("საათი", fontsize=10)
plt.ylabel("საშუალო დეციბელი", fontsize=10)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()