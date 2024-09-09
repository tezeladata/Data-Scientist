import pandas as pd

orders = pd.read_csv("shoefly.csv")
print(orders)

emails = orders.email
print(emails)

frances_palmer = orders[(orders.first_name == "Frances") & (orders.last_name == "Palmer")]
comfy_shoes = orders[orders.shoe_type.isin(["clogs", "boots", "ballet flats"])]
print(comfy_shoes)