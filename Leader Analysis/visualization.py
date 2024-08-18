import numpy as np
import matplotlib.pyplot as plt

data = [['Sandro Jalagonia', 81], ['Giorgi Motsonelidze', 79], ['Giorgi Khmaladze', 75], ['Data Pophkadze', 73], ['Berdia Bekauri', 67], ['Sandro Zabakhidze', 67], ['Giorgi Vanishvili', 65], ['Erekle Kilasonia', 60], ['Aleko Tirkia', 58], ['Shalva Shubitidze', 58], ['Vano Motiashvili', 58], ['Luka Gurgenidze', 56], ['Nikoloz Filishvili', 54], ['Nikoloz Qimeridze', 54], ['Aleksandre Melikjaniani', 52], ['Daniel Abramiani', 52], ['Davit Narimanidze', 52], ['Giorgi Varadashvili', 50], ['Shotiko Nukradze', 50], ['Giorgi Gvritishvili', 48], ['Guram Vakhtangashvili', 46], ['Tsotne Gujabidze', 46], ['Irakli Kvinchia', 46], ['Luka Navrozashvili', 44], ['Zuka Abashidze', 42], ['Mate Dolidze', 40], ['Nikoloz Nutsubidze', 40], ['Mate Giorgelashvili', 37.5], ['Davit Grdzelishvili', 35], ['Nika Kvaracxelia', 35], ['Ucha Khuberishvili', 35], ['Atuka Khuskivadze', 33], ['Gobron Tsitlauri', 33], ['Saba Isakadze', 33], ['Giorgi Shavadze', 31], ['Levani Samsonidze', 31], ['Guram Papunashvili', 27], ['Ilia Dzindzibadze', 23], ['Alex Jimshiashvili', 21], ['Andria Svanidze', 1], ['Giorgi Varazashvili', 1], ['Luka Akofiani', 1], ['Nikoloz Yvavadze', 1], ['Nikoloz Tchitadze', 1]]

names = [item[0] for item in data]
coefficients = [item[1] for item in data]

# Plotting
plt.figure(figsize=(10, 8))
plt.barh(names, coefficients, color='#004225')
plt.xlabel('Neuroticism counter')
plt.ylabel('Squad Leaders')
plt.title('Neuroticism counter for each leader')
plt.suptitle("From best to worst")
plt.gca().invert_yaxis()
plt.grid(axis="x", lw=1)

# Font size
plt.yticks(fontsize=7)

plt.show()