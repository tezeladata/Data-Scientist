import json
import math

with open("wages.json") as json_file:
    data = json.load(json_file)
start_info = [[i["Name"], {"speed count sum": i["Speed 1 Count"] + i["Speed 2 Count"] * 2 + i["Speed 3 Count"] * 3, "Wage": i["Wage"]}, [i["Speed 1 Count"], i["Speed 2 Count"], i["Speed 3 Count"]]] for i in data]

with open("wages2.json") as json_file2:
    data2 = json.load(json_file2)
second_info = [[i["Name"], {"speed count sum": i["Speed 1 count"] + i["Speed 2 count"] * 2 + i["Speed 3 count"] * 3, "Wage": i["Wage"]}, [i["Speed 1 count"], i["Speed 2 count"], i["Speed 3 count"]]] for i in data2]

'''
speed count dependant renewing of wages

<10 , wage = 6.75
10:15 , wage = 7
16:20, wage = 7.25
21:25, wage = 7.5
25:30, wage = 7.75
30:35 , wage = 8 
35:40, wage = 8.25
40:45, wage = 8.5
45:50, wage = 8.75
50 + = giga chad leader , wage = 9
'''


def generate_wages(matrix):
    fin_info = []
    total_sum = 0
    for i in matrix:
        leader, speed_count, speeds = [i[0], {"Old wage": i[1]["Wage"], "Speeds": i[2]}], i[1]["speed count sum"], i[2]

        # 7 good one
        # 6.75 best one

        if speed_count <= 20: wage_per_speed = 6.75
        elif speed_count <= 25: wage_per_speed = 7
        elif speed_count <= 30: wage_per_speed = 7.25
        elif speed_count <= 35: wage_per_speed = 7.5
        elif speed_count <= 40: wage_per_speed = 7.75
        elif speed_count <= 45: wage_per_speed = 8
        elif speed_count <= 50: wage_per_speed = 8.25
        elif speed_count <= 55: wage_per_speed = 8.5
        elif speed_count <= 60: wage_per_speed = 8.75
        elif speed_count <= 65: wage_per_speed = 9
        elif speed_count <= 70: wage_per_speed = 9.25
        elif speed_count <= 75: wage_per_speed = 9.5
        else: wage_per_speed = 9.75

        new_wage = math.ceil(speeds[0] * wage_per_speed + speeds[1] * wage_per_speed * 2 + speeds[2] * wage_per_speed * 2.66)
        wage_diff = new_wage - leader[1]["Old wage"]
        total_sum += wage_diff
        leader[1]["New wage"], leader[1]["Wage increase"] = new_wage, wage_diff

        fin_info.append(leader)

    return fin_info, f"Total wage increase is: {total_sum}"

wage_one = generate_wages(start_info)
wage_two = generate_wages(second_info)


def display(matrix):
    for i in sorted(matrix, reverse=True, key=lambda x: x[1]["New wage"]):
        print(i)

display(wage_one[0])
print(wage_one[1])
print("\n\n")
display(wage_two[0])
print(wage_two[1])