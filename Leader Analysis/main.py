import numpy as np
import matplotlib.pyplot as plt

def visualization(data, x_head, title):
    names = [item[0] for item in data]
    coefficients = [item[1] for item in data]

    # Plotting
    plt.figure(figsize=(10, 8))
    plt.barh(names, coefficients, color='#004225')
    plt.xlabel(x_head)
    plt.ylabel('Squad Leaders')
    plt.title(title)
    plt.suptitle("From best to worst")
    plt.gca().invert_yaxis()
    plt.grid(axis="x", lw=1)

    # Font size
    plt.yticks(fontsize=7)

    plt.show()




leaders = [
["Leader name", "here will be dictionary with OCEAN quiz scores"],
["Aleko Tirkia", {"O": 83, "C": 71, "E": 60, "A": 48, "N": 58}],
["Aleksandre Melikjaniani", {"O": 52, "C": 48, "E": 54, "A": 58, "N": 52}],
["Andria Svanidze", {"O": 1, "C": 1, "E": 1, "A": 1, "N": 1}], #aaaaa
["Atuka Khuskivadze", {"O": 62.5, "C": 73, "E": 52, "A": 50, "N": 33}],
["Berdia Bekauri", {"O": 75, "C": 71, "E": 73, "A": 77, "N": 67}],
["Daniel Abramiani", {"O": 60, "C": 69, "E": 73, "A": 48, "N": 52}],
["Data Pophkadze", {"O": 48, "C": 56, "E": 65, "A": 79, "N": 73}],
["Davit Grdzelishvili", {"O": 85, "C": 75, "E": 73, "A": 71, "N": 35}],
["Davit Narimanidze", {"O": 85, "C": 87.5, "E": 60, "A": 96, "N": 52}],
["Erekle Kilasonia", {"O": 56, "C": 40, "E": 44, "A": 56, "N": 60}],
["Giorgi Gvritishvili", {"O": 58, "C": 54, "E": 54, "A": 65, "N": 48}],
["Giorgi Motsonelidze", {"O": 71, "C": 54, "E": 65, "A": 73, "N": 79}],
["Giorgi Shavadze", {"O": 67, "C": 79, "E": 77, "A": 60, "N": 31}],
["Giorgi Vanishvili", {"O": 60, "C": 58, "E": 12.5, "A": 48, "N": 65}],
["Giorgi Varadashvili", {"O": 69, "C": 60, "E": 75, "A": 73, "N": 50}],
["Giorgi Varazashvili", {"O": 67, "C": 96, "E": 75, "A": 87.5, "N": 37.5}],
["Gobron Tsitlauri", {"O": 100, "C": 62.5, "E": 65, "A": 75, "N": 33}],
["Guram Papunashvili", {"O": 71, "C": 62.5, "E": 58, "A": 46, "N": 27}],
["Guram Vakhtangashvili", {"O": 67, "C": 79, "E": 73, "A": 69, "N": 46}],
["Ilia Dzindzibadze", {"O": 75, "C": 94, "E": 54, "A": 62.5, "N": 23}],
["Levani Samsonidze", {"O": 67, "C": 77, "E": 48, "A": 52, "N": 31}],
["Luka Akofiani", {"O": 69, "C": 58, "E": 46, "A": 52, "N": 50}],
["Luka Gurgenidze", {"O": 75, "C": 94, "E": 42, "A": 54, "N": 56}],
["Luka Navrozashvili", {"O": 79, "C": 75, "E": 77, "A": 81, "N": 44}],
["Mate Dolidze", {"O": 83, "C": 58, "E": 65, "A": 58, "N": 40}],
["Mate Giorgelashvili", {"O": 77, "C": 67, "E": 46, "A": 52, "N": 37.5}],
["Nikoloz Filishvili", {"O": 81, "C": 50, "E": 58, "A": 46, "N": 54}],
["Nikoloz Nutsubidze", {"O": 75, "C": 85, "E": 65, "A": 75, "N": 40}],
["Nikoloz Qimeridze", {"O": 77, "C": 62.5, "E": 58, "A": 52, "N": 54}],
["Nikoloz Yvavadze", {"O": 69, "C": 48, "E": 54, "A": 73, "N": 62.5}], 
["Saba Isakadze", {"O": 71, "C": 71, "E": 71, "A": 69, "N": 33}],
["Sandro Jalagonia", {"O": 56, "C": 33, "E": 25, "A": 69, "N": 81}],
["Sandro Zabakhidze", {"O": 90, "C": 52, "E": 40, "A": 62.5, "N": 67}],
["Shalva Shubitidze", {"O": 67, "C": 33, "E": 48, "A": 69, "N": 58}],
["Shotiko Nukradze", {"O": 69, "C": 58, "E": 75, "A": 62.5, "N": 50}],
["Tsotne Gujabidze", {"O": 58, "C": 85, "E": 42, "A": 62.5, "N": 46}],
["Nika Kvaracxelia", {"O": 79, "C": 75, "E": 69, "A": 65, "N": 35}],
["Vano Motiashvili" ,{"O": 71, "C": 58, "E": 31, "A": 71, "N": 58}],
["Zuka Abashidze", {"O": 81, "C": 79, "E": 48, "A": 65, "N": 42}],
["Nikoloz Tchitadze", {"O": 62.5, "C": 62.5, "E": 77, "A": 62.5, "N": 35}],
["Irakli Kvinchia", {"O": 69, "C": 81, "E": 60, "A": 79, "N": 46}],
["Ucha Khuberishvili", {"O": 60, "C": 85, "E": 54, "A": 85, "N": 35}],
["Alex Jimshiashvili", {"O": 87.5, "C": 100, "E": 79, "A": 52, "N": 21}],
["Giorgi Khmaladze", {"O": 69, "C": 75, "E": 50, "A": 79, "N": 75}]
]

github_data = [
    "fine per student - fps, final fine, not written info count, standing in sorted list",
    [1.25, 5, 0, 18], [0, 0, 0, 0], [2, 13, 0, 19], [4.272727273, 47, 0, 29],
    [4.142857143, 29, 1, 36], [1.043478261, 24, 0, 5], [1.710526316, 32.5, 0, 12], [6.465517241, 375, 1, 24],
    [4.159090909, 91.5, 0, 22], [2.222222222, 40, 0, 25], [1.8125, 14.5, 0, 34], [1.222222222, 11, 0, 9], 
    [2.166666667, 39, 0, 26], [0.7608695652, 17.5, 0, 3], [7.333333333, 44, 0, 37], [3.571428571, 25, 0, 35],
    [5.5, 60.5, 0, 38], [2.403225806, 74.5, 1, 20], [4.421052632, 168, 38, 23], [0.7142857143, 10, 0, 8],
    [1.115384615, 29, 1, 10], [13, 143, 0, 33], [0.7, 14, 0, 4], [4.454545455, 49, 0, 31],
    [6.823529412, 116, 0, 32], [0.4166666667, 7.5, 0, 1], [1.5, 15, 0, 16], [0, 0, 0, 7],
    [0, 0, 0, 39], [3, 45, 0, 27], [0, 0, 0, 6], [3.285714286, 23, 0, 30], 
    [0.8, 16, 0, 2], [1, 19, 0, 13], [1, 16, 0, 15], [0.9333333333, 14, 0, 14], 
    [1.125, 9, 0, 17], [1.25, 35, 0, 11], [3.28, 82, 0, 21], [0, 0, 0, 40], 
    [0, 0, 0, 41], [0, 0, 0, 42], [0, 0, 0, 43], [0, 0, 0, 44]
]


'''
Combine leaders with their github data
'''
all_data = [[leaders[i], github_data[i]] for i in range(1, len(leaders))]


'''
Function for sorting, you have to adjust info: O/C/E/A/N
'''
def data_sort(data_key):
    return sorted(leaders[1:], key=lambda x: x[1][data_key], reverse=True)

openness = data_sort("O")
conscientiousness = data_sort("C")
extraversion = data_sort("E")
agreeableness = data_sort("A")
neuroticism = data_sort("N")


'''
conscientiousness correlation to fine per student - fps
'''
def cor1(data):
    all_res = []

    for i in data:
        name = i[0][0] 
        c = i[0][1]["C"] 
        fps = i[1][0]  

        # Define thresholds for high/low values
        c_threshold = 75
        fps_threshold = 2

        # ZeroDivisionError
        if fps == 0:
            if c >= c_threshold:
                result = c * 1.5
            else:
                result = c / 2  
        else:
            if c <= c_threshold and fps >= fps_threshold:
                result = (c * fps) * 0.5   # Strong correlation
            elif c >= c_threshold and fps >= fps_threshold:
                result = (c * fps) ** 0.5  # Moderate correlation
            elif c < c_threshold and fps >= fps_threshold:
                result = fps / c * 0.5  # Weak correlation
            else:
                result = (c * fps) ** 0.5 # Moderate correlation

        all_res.append([name, result])

    return sorted(all_res, key=lambda x: x[1])

visualization(cor1(all_data), "მაჩვენებელი დაბალი - C მაღალი, fine per student (fps) დაბალი. მაჩვენებელი მაღალი - C დაბალი, fps მაღალი", "C correlation to fine per student")