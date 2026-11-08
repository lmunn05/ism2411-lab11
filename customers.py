# Self assesment questions -

# 1. I would use .get() when a dictionary key might not exist because it prevents errors and allows me to set a default value. I would use bracket notation when I know the key exists and need to access its value directly. My rule of thumb is to use .get() for optional information and brackets for required information.

# 2. Building a summary dictionary in Python reminds me of using PivotTables in Excel because both can group data and calculate totals. Python can be more useful for large datasets because it can automate the process and handle large amounts of data without manually organizing everything in Excel.


print ("--- Exercise 1 ---")
customer = {
    "name":"Alice", # Key value,
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
    }

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])


print("--- Exercise 2 ---")
customer['phone'] = '555-5555' # Adding a new key value pair to dictionary
print(customer)
customer['tier'] = 'platinum'
print(customer)
del customer['name']
print(customer)

print(customer.get('yd_spend',0))

print("--- Exercise 3 --- ")
print(customer.get("email", "no email on file"))

print("---Exercise 4 ---")

for key in customer:
    print(customer.get("email","no email on file"))

for something in customer:
    print(something, customer[something])

print("---Exercise 5---")
tier_discounts= {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1-discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount_rate * 100}%")
print(f"Final price ${final_price:.2f}")

print("--- Exercise 6 ---")
customers= [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750 }
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a 300 dollar purchase")

print(" ---Exercise 7---")
catalog= {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name, product_details in catalog.items():
    if product_details["stock"]< 20:
        print(f"LOW STOCK: {product_name}- only {product_details['stock']} left")

print("---Exercise 8---")

print("--- Exercise 8 ---")

transactions = [
    {"region": "North", "sales": 500},
    {"region": "South", "sales": 750},
    {"region": "North", "sales": 300},
    {"region": "East", "sales": 900},
    {"region": "South", "sales": 250}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["sales"]

    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region, total in sales_by_region.items():
    print(f"{region}: ${total:.2f}")
