
'''
for extra variable
'''
# def cor1(data):
#     all_res = []

#     for i in data:
#         name = i[0][0] 
#         c = i[0][1]["C"] 
#         fps = i[1][0]  

#         # Define thresholds for high/low values
#         c_threshold = 75
#         fps_threshold = 2

#         # ZeroDivisionError
#         if fps == 0:
#             if c >= c_threshold:
#                 result = c * 1.5
#             else:
#                 result = c / 2  
#         else:
#             if c <= c_threshold and fps >= fps_threshold:
#                 result = (c * fps) * 0.5   # Strong correlation
#             elif c >= c_threshold and fps >= fps_threshold:
#                 result = (c * fps) ** 0.5  # Moderate correlation
#             elif c > c_threshold and fps >= fps_threshold:
#                 result = fps / c * 0.5  # Weak correlation
#             else:
#                 result = (c * fps) ** 0.5 # Moderate correlation

#         all_res.append([name, c, fps])

#     return sorted(all_res, key=lambda x: x[1])

# visualization(cor1(all_data), "conscientiousness", "fine per student")


'''
Function for sorting, you have to adjust info: O/C/E/A/N
'''
# def data_sort(data_key):
#     return sorted(leaders[1:], key=lambda x: x[1][data_key], reverse=True)

# openness = data_sort("O")
# conscientiousness = data_sort("C")
# extraversion = data_sort("E")
# agreeableness = data_sort("A")
# neuroticism = data_sort("N")





'''
Extra
'''
# def two_ocean_data(data, var2):
#     all_res = []

#     for i in data:
#         if i[1][0] > 0 and i[1][1] < 150 and i[1][4] > 5:
#             name = i[0][0] 
#             ocean_var = (i[0][1]["O"] * i[0][1]["C"]) ** 0.5
#             match var2:
#                 case "fps": y_row_data = i[1][0]
#                 case "ff": y_row_data = i[1][1]
#                 case "nwic": y_row_data = i[1][2]
#                 case "sisl": y_row_data = i[1][3]
#                 case "mc": y_row_data = i[1][4]

#             all_res.append([name, ocean_var, y_row_data])

#     return sorted(all_res, key=lambda x: x[1])
# def two_github_data(data):
#     all_res = []

#     for i in data:
#         if i[1][0] > 0 and i[1][1] < 150 and i[1][3] > 5:
#             name = i[0][0] 
#             x_data = i[1][3]
#             y_data = i[1][0]

#             all_res.append([name, x_data, y_data])

#     return sorted(all_res, key=lambda x: x[1])



'''
correlation
'''
# def all(data, var, var2):
#     all_res = []

#     for i in data:
#         if i[1][0] > 0 and i[1][1] < 100 and i[1][3] > 5 and i[0]!= "Luka Akofiani":
#             name = i[0][0] 
#             ocean_var = i[0][1][f"{var}"] 
#             match var2:
#                 case "fps": y_row_data = i[1][0]
#                 case "ff": y_row_data = i[1][1]
#                 case "sisl": y_row_data = i[1][2]
#                 case "mc": y_row_data = i[1][3]

#             all_res.append([name, ocean_var, y_row_data])

#     return sorted(all_res, key=lambda x: x[1])


# def visualization(data, x_head, y_head):
#     names = [item[0].split(" ")[1] for item in data]
#     x_values = [item[1] for item in data]
#     y_values = [item[2] for item in data]

#     # Plotting
#     plt.figure(figsize=(10, 8))
#     plt.scatter(x_values, y_values, color='#004225')
#     plt.scatter(x_values, y_values, color='#004225')

#     for i, name in enumerate(names):
#         plt.text(x_values[i], y_values[i], name, fontsize=10, ha='right')

#     # Adding linear regression line
#     m, b = np.polyfit(x_values, y_values, 1)  # Fit line: y = mx + b
#     plt.plot(x_values, np.array(x_values) * m + b, color='red', linestyle='--', linewidth=2)

#     plt.xlabel(x_head)
#     plt.ylabel(y_head)
#     plt.title("Leader analysis")
#     plt.grid(True)

#     plt.show()



# good
# visualization(all(all_data, "E", "sisl"), "extraversion", "standing in sorted list")
# visualization(all(all_data, "E", "mc"), "extraversion", "member count")
# visualization(all(all_data, "E", "fps"), "extraversion", "fine per student")
# visualization(all(all_data, "O", "ff"), "openness", "final fine")
# visualization(all(all_data, "A", "ff"), "agreeableness", "final fine")
# visualization(all(all_data, "A", "fps"), "agreeableness", "fine per student")
# visualization(all(all_data, "A", "sisl"), "agreeableness", "standing in sorted list")
# visualization(all(all_data, "A", "mc"), "agreeableness", "member count")
# visualization(all(all_data, "N", "ff"), "neuroticism", "final fine")
# visualization(all(all_data, "N", "sisl"), "neuroticism", "standing in sorted list")

# bad
# visualization(all(all_data, "E", "ff"), "extraversion", "final fine")
# visualization(all(all_data, "O", "fps"), "openness", "fine per student")
# visualization(all(all_data, "O", "sisl"), "openness", "standing in sorted list")
# visualization(all(all_data, "O", "mc"), "openness", "member count")
# visualization(all(all_data, "C", "ff"), "conscientiousness", "final fine")
# visualization(all(all_data, "C", "fps"), "conscientiousness", "fine per student")
# visualization(all(all_data, "C", "sisl"), "conscientiousness", "standing in sorted list")
# visualization(all(all_data, "C", "mc"), "conscientiousness", "member count")
# visualization(all(all_data, "N", "fps"), "neuroticism", "fine per student")
# visualization(all(all_data, "N", "mc"), "neuroticism", "member count")