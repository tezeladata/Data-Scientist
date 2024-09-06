import json
import math

with open("wages.json") as json_file:
    data = json.load(json_file)

start_info = [[i["Name"], {"speed count sum": i["Speed 1 Count"] + i["Speed 2 Count"] * 2 + i["Speed 3 Count"] * 3, "Wage": i["Wage"]}, [i["Speed 1 Count"], i["Speed 2 Count"], i["Speed 3 Count"]]] for i in data]

'''
speed count dependant renewing of wages

< 20 - Loser leader - wage per speed = 7.5
< 35 - mid leader - wage per speed = 8
< 50 - chad leader - wage per speed = 8.5
>= 50 - giga leader - wage per speed = 9
'''

fin_info = []
total_sum = 0
for i in start_info:
    leader, speed_count, speeds = [i[0], {"Old wage": i[1]["Wage"], "Speeds": i[2]}], i[1]["speed count sum"], i[2]

    if speed_count < 20: wage_per_speed = 7.5
    elif speed_count < 35: wage_per_speed = 8.5
    elif speed_count < 50: wage_per_speed = 9.5
    else: wage_per_speed = 10.5

    new_wage = math.ceil(speeds[0]*wage_per_speed + speeds[1]*wage_per_speed*2 + speeds[2]*wage_per_speed*2.66)
    wage_diff = new_wage - leader[1]["Old wage"]
    total_sum += wage_diff
    leader[1]["New wage"], leader[1]["Wage increase"] = new_wage, wage_diff

    fin_info.append(leader)

for i in fin_info:
    print(i)
print(f"In total, wage gain sum for all leaders is: {total_sum}")


# for distribution
# def count_sums(matrix):
#     res = []
#     for i in matrix: res.append([i[0], {"speed count":  i[1]["speed count sum"]}])
#
#     return sorted(res, key=lambda x: x[1]["speed count"], reverse=True)
#
# dist = count_sums(start_info)
# for i in dist:
#     print(i)