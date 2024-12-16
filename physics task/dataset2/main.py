import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file - source - Official Portal of the UAE Government
first = pd.read_csv("abu-dhabi.csv")

# Calculate the mean of each station location
average_noise = (
    first.groupby("Station_Location")["Average_Noise_Level (decibels) (historical data has been modified from data source)"]
    .mean()
    .reset_index()
)

# Renaming columns for better readability
average_noise.rename(
    columns={"Average_Noise_Level (decibels) (historical data has been modified from data source)": "Average_Noise_Level"},
    inplace=True
)

# Plotting the data
plt.figure(figsize=(12, 8))
plt.barh(
    average_noise["Station_Location"],
    average_noise["Average_Noise_Level"],
    color="skyblue",
    edgecolor="black"
)
plt.xlabel("დეციბელი", fontsize=12)
plt.ylabel("ქალაქის ნაწილი", fontsize=12)
plt.title("საშუალო ხმის დონე ქალაქის ნაწილების მიხედვით (დეციბელი)", fontsize=14)
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()