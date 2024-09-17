# In order to efficiently store data, we often spread related information across multiple tables.
# However, a lot of this information would be repeated. If the same customer makes multiple orders, that customer’s name, address, and phone number will be reported multiple times. If the same product is ordered by multiple customers, then the product price and description will be repeated. This will make our orders table big and unmanageable.

# So instead, we can split our data into three tables:
# orders would contain the information necessary to describe an order: order_id, customer_id, product_id, quantity, and timestamp
# products would contain the information to describe each product: product_id, product_description and product_price
# customers would contain the information for each customer: customer_id, customer_name, customer_address, and customer_phone_number

import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)
customers = pd.read_csv('customers.csv')
print(customers)


# The .merge() method looks for columns that are common between two DataFrames and then looks for rows where those column’s values are the same. It then combines the matching rows into a single row in a new table.
# However, when we are using more than 2 DataFrames, we can merge in following way:
df_main = orders.merge(products).merge(customers)
print(df_main)


# When we combine tables and same column names mean different things, for example "id" - we can rename column of any table
df_second = pd.merge(orders, products.rename(columns={"id": "customer_id"}))
print(df_second)



# If we don’t want to do that, we have another option. We could use the keywords left_on and right_on to specify which columns we want to perform the merge on. In the example below, the “left” table is the one that comes first (orders), and the “right” table is the one that comes second (customers). This syntax says that we should match the customer_id from orders to the id in customers.
# If we use this syntax, we’ll end up with two columns called id, one from the first table and one from the second. Pandas won’t let you have two columns with the same name, so it will change them to id_x and id_y.
# The new column names id_x and id_y aren’t very helpful for us when we read the table. We can help make them more useful by using the keyword suffixes. We can provide a list of suffixes to use instead of “_x” and “_y”.
# orders = pd.read_csv('orders.csv')
# print(orders)
# products = pd.read_csv('products.csv')
# print(products)
# orders_products = pd.merge(
#   orders,
#   products,
#   left_on = "product_id",
#   right_on = "id",
#   suffixes = ["_orders", "_products"]
# )
# print(orders_products)


# The type of merge where we only include matching rows is called an inner merge. There are other types of merges that we can use when we want to keep information from the unmatched rows.
# An Outer Join would include all rows from both tables, even if they don’t match. Any missing values are filled in with None or nan (which stands for “Not a Number”).
# pd.merge(company_a, company_b, how='outer')

# Example of outer join:
store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)
store_a_b_outer=pd.merge(store_a, store_b, how="outer")
print(store_a_b_outer)

# A Left Merge includes all rows from the first (left) table, but only rows from the second (right) table that match the first table.
# pd.merge(company_a, company_b, how='left')
# Right merge is the exact opposite of left merge. Here, the merged table will include all rows from the second (right) table, but only rows from the first (left) table that match the second table.
# pd.merge(company_a, company_b, how="right")


# When two or more tables have same column names, we can use concat method to concatenate tables
bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)
menu = pd.concat([bakery, ice_cream])
print(menu)