with open('main.txt') as text:
    content = text.read()
print(content)


# printing only lines
# Using .readlines() function
with open('main.txt') as text:
    for line in text.readlines():
        print(line)

# Using readline for only one line at a time
with open('main.txt') as text:
    lines = [text.readline() for i in range(len(text.readline()))]

# Only first line
with open('main.txt') as text:
    first_line = text.readline().split(".")
for line in first_line: print(line, end="\n")


# Writing files
with open("test.txt", "w") as new_text:
    new_text.write("Hello World")

# appending text to already created file
with open('test.txt', 'a') as new_text:
    new_text.write("\n... Hello World")

# for csv - comma-separated-values file
with open("business-financial-data-march-2024-csv.csv") as csv_file:
    print(csv_file.read())

# improved reading of csv file
import csv

res, res2 = [], []
with open("users.csv", newline="") as new_csv:
    dict1 = csv.DictReader(new_csv)
    for row in dict1:
        res.append(row)
        res2.append(row["Email"])

print(res, res2)


# csv with different delimeter
with open("addresses.csv", newline="") as new_csv:
    dict1 = csv.DictReader(new_csv, delimiter=";")
    for row in dict1: print(row)


# writing csv
big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}]

import csv

with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)

  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)

