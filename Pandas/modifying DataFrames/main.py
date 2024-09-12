import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Adding info for each individual item
df["Sold in Bulk?"] = ["Yes", "Yes", "No", "No"]

# Adding info in easier way
df["In Stock?"] = "Yes"
df["Is taxed?"] = "Yes"
print(df)


# We can also add new column and info will be based on previous columns' info
df2 = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

df2["Margin"] = df2.Price - df2['Cost to Manufacture']
print(df2)


# We can use method, called "apply" for easier way to renew information
df3 = pd.DataFrame([
    [1, "david tezelashvili", 16],
    [2, "andria tezelashvili", 9]
], columns=["ID", "Full name", "Age"])
# We want to capitalize all full names
df3["Full name"] = df3["Full name"].apply(str.capitalize)
print(df3)



# Review of lambda
# lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]



# using lambda function to create new column
df4 = pd.read_csv("employees.csv")
df4["Last Name"] = df4.name.apply(lambda x: x.split(" ")[-1])
print(df4)


# We can also operate on multiple columns at once. If we use apply without specifying a single column and add the argument axis=1, the input to our lambda function will be an entire row, not a column.
# To access particular values of the row, we use the syntax row.column_name or row[‘column_name’].


# We can easily change column names of out DataFrame with following method:
df4.columns = ["ID", "Person_Name", "Hourly_Wage", "Hours_Worked", "Last_Name"]
print(df4)


# We can easily change names of individual columns using following method:
df4.rename(columns={
    "ID": "id"
}, inplace=True)
# If we do not want to create new DataFrame, we write inplace=True
print(df4)


# Review:

orders = pd.read_csv('shoefly.csv')
orders['shoe_source'] = orders.shoe_material.apply(lambda x: 'animal' if x == 'leather'else 'vegan')
orders['salutation'] = orders.apply(lambda row: 'Dear Mr. ' + row['last_name'] if row['gender'] == 'male' else 'Dear Ms. ' + row['last_name'], axis=1)
print(orders)