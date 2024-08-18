
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