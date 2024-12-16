import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file - source - WHO
first = pd.read_csv("over50decib.csv")

# arrays for road and rail data
road_data = first[first["EXPOSURE_NOISE"] == "ROAD"]
road = road_data[["COUNTRY", "VALUE"]].dropna().sort_values(by="VALUE", ascending=True)
rail_data = first[first["EXPOSURE_NOISE"] == "RAIL"]
rail = rail_data[["COUNTRY", "VALUE"]].dropna().sort_values(by="VALUE", ascending=True)

# ფუნქცია ნახაზის შესაქმნელად
def plot_dataset1(fortitle, xrow_data, yrow_data):
    plt.figure(figsize=(12, 8))
    plt.barh(xrow_data, yrow_data, color="skyblue", edgecolor="black")
    plt.xlabel("პროცენტული მაჩვენებელი", fontsize=12)
    plt.ylabel("ქვეყანა", fontsize=12)
    plt.title(fortitle, fontsize=14)
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.show()

# Plot1 - მოსახლეობის რამდენი პროცენტი ისმენს 50 დეციბელზე მაღალი დონის ხმაურს საგზაო ხმაურიდან
plot_dataset1(fortitle="მოსახლეობის რამდენი პროცენტი ისმენს 50 დეციბელზე მაღალი დონის ხმაურს საგზაო ხმაურიდან", xrow_data=road["COUNTRY"].values, yrow_data=road["VALUE"].values)
# Plot2 - მოსახლეობის რამდენი პროცენტი ისმენს 50 დეციბელზე მაღალი დონის ხმაურს სარკინიგზო ხმაურიდან
plot_dataset1(fortitle="მოსახლეობის რამდენი პროცენტი ისმენს 50 დეციბელზე მაღალი დონის ხმაურს სარკინიგზო ხმაურიდან", xrow_data=rail["COUNTRY"].values, yrow_data=rail["VALUE"].values)

# 50 დეციბელი და უფრო მეტი - ძილის ხარისხის დაწევა, ჰიპერტენზია, გულის დაავადებების რისკის ზრდა, სტრესის ჰორმონის დონის მომატება, მარტივი გაღიზიანებადობა, სმენის პრობლემები