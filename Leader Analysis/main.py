import numpy as np
import matplotlib.pyplot as plt

leaders = [
["Leader name", "here will be dictionary with OCEAN quiz scores"],
["Aleko Tirkia", {"O": 83, "C": 71, "E": 60, "A": 48, "N": 58}],
["Aleksandre Melikjaniani", {"O": 52, "C": 48, "E": 54, "A": 58, "N": 52}],
["Andria Svanidze", {"O": 77, "C": 63, "E": 63, "A": 77, "N": 48}],
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
["Giorgi Khmaladze", {"O": 69, "C": 75, "E": 50, "A": 79, "N": 75}],
# from here
["Nika Gelenidze", {"O": 75, "C": 94, "E": 67, "A": 50, "N": 52}],
["Leqso Leverashvili", {"O": 73, "C": 92, "E": 67, "A": 83, "N": 42}],
["Davit Janashia", {"O": 62.5, "C": 62.5, "E": 50, "A": 65, "N": 48}],
["Nia Khoperia", {"O": 48, "C": 54, "E": 56, "A": 67, "N": 67}],
["Roba Amonashvili", {"O": 71, "C": 52, "E": 48, "A": 71, "N": 62.5}],
["Barbare Tinikashvili", {"O": 60, "C": 81, "E": 54, "A": 65, "N": 31}],
["Jeko Tarieladze", {"O": 62.5, "C": 50, "E": 46, "A": 81, "N": 85}],
["Gigi Adamia", {"O": 90, "C": 90, "E": 75, "A": 54, "N": 46}],
["Davit Berkacashvili", {"O": 79, "C": 71, "E": 56, "A": 69, "N": 54}],
["Nika Shavadze", {"O": 65, "C": 83, "E": 48, "A": 65, "N": 33}],
["Tato Bukhrashvili", {"O": 62.5, "C": 58, "E": 50, "A": 54, "N": 60}],
["Ana Grigolia", {"O": 75, "C": 56, "E": 37.5, "A": 92, "N": 42}],
["Giorgi Melqadze", {"O": 67, "C": 54, "E": 42, "A": 65, "N": 54}],
["Luka Oqruashvili", {"O": 71, "C": 58, "E": 42, "A": 71, "N": 54}],
["Gigi Bendeliani", {"O": 71, "C": 67, "E": 54, "A": 60, "N": 44}]
]

github_data = [
    "fine per student - fps, final fine, standing in sorted list, member count",
    [1.25, 5, 18, 4], [0, 0, 0, 5], [2, 13, 19, 6], [4.272727273, 47, 29, 11],
    [4.142857143, 29, 36, 7], [1.043478261, 24, 5, 23], [1.710526316, 32.5, 12, 19], [6.465517241, 375, 24, 58],
    [4.159090909, 91.5, 22, 22], [2.222222222, 40, 25, 18], [1.8125, 14.5, 34, 8], [1.222222222, 11, 9, 11], 
    [2.166666667, 39, 26, 17], [0.7608695652, 17.5, 3, 23], [7.333333333, 44, 37, 6], [3.571428571, 25, 35, 7],
    [5.5, 60.5, 38, 11], [2.403225806, 74.5, 20, 31], [4.421052632, 168, 23, 38], [0.7142857143, 10, 8, 14],
    [1.115384615, 29, 10, 26], [13, 143, 33, 11], [0.7, 14, 4, 20], [4.454545455, 49, 31, 11],
    [6.823529412, 116, 32, 17], [0.4166666667, 7.5, 1, 18], [1.5, 15, 16, 10], [0, 0, 7, 9],
    [0, 0, 39, 7], [3, 45, 27, 15], [0, 0, 6, 15], [3.285714286, 23, 30, 7], 
    [0.8, 16, 2, 20], [1, 19, 13, 18], [1, 16, 15, 10], [0.9333333333, 14, 14, 13], 
    [1.125, 9, 17, 8], [1.25, 35, 11, 28], [3.28, 82, 21, 25], [0, 0, 40, 0], 
    [0, 0, 41, 0], [0, 0, 42, 0], [0, 0, 43, 0], [0, 0, 44, 0],
    # from here
    [3.055555555555556, 82.5, 45, 27], [5.5, 22, 46, 4], [5.75, 172.5, 47, 30], [0.8666666666666667, 15, 48, 13],
    [2.25, 9, 49, 4], [2.088235294117647, 35.5, 49, 17], [1.4, 21, 50, 15], [1.166666666666667, 3.5, 51, 3],
    [0.6875, 11, 52, 16], [0 , 0, 52, 3], [4.910714285714286, 137.5, 53, 28], [13.21428571428571, 92.5, 53, 7], 
    [1.866666666666667, 28, 54, 15], [2.388888888888889, 43, 55, 18], [0, 0, 56, 2]
]


'''
Combine leaders with their github data
'''
all_data = [[leaders[i], github_data[i]] for i in range(1, len(leaders))]



# Define the all function
def all(data, var, var2):
    all_res = []
    for i in data:
        if i[1][0] > 0 and i[1][1] < 100 and i[1][3] > 5 and i[0] != "Luka Akofiani":
            name = i[0][0] 
            ocean_var = i[0][1][f"{var}"]
            match var2:
                case "fps": y_row_data = i[1][0]
                case "ff": y_row_data = i[1][1]
                case "sisl": y_row_data = i[1][2]
                case "mc": y_row_data = i[1][3]
            all_res.append([name, ocean_var, y_row_data])
    return sorted(all_res, key=lambda x: x[1])

# Define the visualization function
def visualization(data_before, data_after, x_head, y_head):
    names_before = [item[0].split(" ")[1] for item in data_before]
    x_values_before = [item[1] for item in data_before]
    y_values_before = [item[2] for item in data_before]
    
    names_after = [item[0].split(" ")[1]  for item in data_after]
    x_values_after = [item[1] for item in data_after]
    y_values_after = [item[2] for item in data_after]


    plt.figure(figsize=(12, 8))
    
    plt.scatter(x_values_before, y_values_before, color='blue', label='Prev leaders', alpha=0.7)
    for i, name in enumerate(names_before):
        plt.text(x_values_before[i], y_values_before[i], name, fontsize=10, ha='right')


    plt.scatter(x_values_after, y_values_after, color='green', label='Cur leaders', alpha=0.7)
    for i, name in enumerate(names_after):
        plt.text(x_values_after[i], y_values_after[i], name, fontsize=8, ha='left')


    x_all = x_values_before + x_values_after
    y_all = y_values_before + y_values_after
    m, b = np.polyfit(x_all, y_all, 1)  
    plt.plot(x_all, np.array(x_all) * m + b, color='red', linestyle='--', linewidth=2)

    plt.xlabel(x_head)
    plt.ylabel(y_head)
    plt.title("Leader Analysis")
    plt.grid(True)
    plt.legend()
    plt.show()



split_index = 43  
before_data = all_data[:split_index]
after_data = all_data[split_index:]

before_plot_data = all(before_data, 'C', 'mc')
after_plot_data = all(after_data, 'C', 'mc')

visualization(before_plot_data, after_plot_data, 'OCEAN Score - C', 'Member count (mc)')