import csv


# Accessing csv file:
data = []
with open("insurance.csv") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader: data.append(row)


# Calculate average age:
def get_avg(all): return sum(int(person["age"]) for person in all) / len(all)
print(f"\nAverage age for all patients are: {get_avg(data)}\n")


# Calculate regions:
def get_regions(all):
    places = {}
    for person in all:
        place = person["region"]

        if place not in places.keys(): places[place] = 1
        else: places[place] += 1

    return places
all_regions = get_regions(data)
print(f"\nDistribution of all patients: {all_regions}\n")


# Most spread region:
def get_best_region(all_regions):
    for region, count in all_regions.items():
        if count == max(all_regions.values()): return region
print(f"\nMost patients come from {get_best_region(all_regions).capitalize()} region\n")


# Charges for smokers vs non smokers:
def get_charges(all):
    smokers, nonsmokers = [], []

    for person in all:
        match person["smoker"]:
            case "yes": smokers.append(float(person["charges"]))
            case "no": nonsmokers.append(float(person["charges"]))

    return smokers, nonsmokers
charges_data = get_charges(data)
print(f"\nTotal charge for all smokers are: {sum(charges_data[0])}\nOn average, smoker gets charge of: {sum(charges_data[0]) / len(charges_data[0])}")
print(f"\nTotal charge for all nonsmokers are: {sum(charges_data[1])}\nOn average, nonsmoker gets charge of: {sum(charges_data[1]) / len(charges_data[1])}\n")


# Bmi - smoker/nonsmoker correlation:
def get_cor(all):
    smokers, nonsmokers = [], []
    for person in all:
        if isinstance(person, dict):
            if person.get("smoker") == "yes":
                smokers.append(float(person.get("bmi")))
            elif person.get("smoker") == "no":
                nonsmokers.append(float(person.get("bmi")))

    average_smoker_bmi = sum(smokers) / len(smokers) if smokers else 0
    average_nonsmoker_bmi = sum(nonsmokers) / len(nonsmokers) if nonsmokers else 0

    return average_smoker_bmi, average_nonsmoker_bmi
print(f"\nAverage bmi for smoker is: {get_cor(data)[0]} and average bmi for nonsmoker is: {get_cor(data)[1]}\n")


# Age-child correlation
def get_cor2(all):
    filtered_data = [person for person in all if int(person["children"]) > 0]
    total_age = sum(int(person["age"]) for person in filtered_data)
    average_age = total_age / len(filtered_data) if filtered_data else 0

    return average_age


print(f"\nFor person to have at least one children, their age is {get_cor2(data)}\n")