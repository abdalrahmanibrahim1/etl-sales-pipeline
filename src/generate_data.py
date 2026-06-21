# Imports
import pandas as pd
import random
from pathlib import Path
from datetime import datetime, timedelta


# Configuration
RAW_DATA_PATH = Path("data/raw")
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)
random.seed(42)


# Reference Data
cities = [
    "Amman",
    "Zarqa",
    "Irbid",
    "Aqaba",
    "Salt",
    "Madaba"
]

#Create products
products_data = [
    ("P001", "Laptop", "Electronics", 800),
    ("P002", "Mouse", "Electronics", 20),
    ("P003", "Keyboard", "Electronics", 45),
    ("P004", "Monitor", "Electronics", 220),
    ("P005", "Desk Chair", "Furniture", 150),
    ("P006", "Desk", "Furniture", 300),
    ("P007", "Notebook", "Stationery", 3),
    ("P008", "Pen Pack", "Stationery", 5),
    ("P009", "Backpack", "Accessories", 40),
    ("P010", "USB Cable", "Electronics", 10),
    ("P011", "Headphones", "Electronics", 90),
    ("P012", "Webcam", "Electronics", 70),
    ("P013", "Printer", "Electronics", 180),
    ("P014", "Office Lamp", "Furniture", 35),
    ("P015", "Whiteboard", "Stationery", 60),
    ("P016", "Tablet", "Electronics", 350),
    ("P017", "Phone Stand", "Accessories", 15),
    ("P018", "External Hard Drive", "Electronics", 120),
    ("P019", "Water Bottle", "Accessories", 12),
    ("P020", "Calculator", "Stationery", 25)
]


# Generate Customers
customers = []

for i in range(1, 1001):
    customer_id = f"C{i:03}"
    name = f"Customer {i}"
    city = random.choice(cities)
    signup_date = datetime(2024, 1, 1) + timedelta(
        days=random.randint(0, 365)
    )

    customer = {
        "customer_id": customer_id,
        "name": name,
        "city": city,
        "signup_date": signup_date
    }

    customers.append(customer)

#Adding messy data to customers table
customers.append({
    "customer_id": "C9999",
    "name": None,
    "city": "Amman",
    "signup_date": datetime(2024, 1, 1)
})
customers.append({
    "customer_id": None,
    "name": "No ID Customer",
    "city": "Amman",
    "signup_date": datetime(2024, 2, 1)
})

customers.append({
    "customer_id": "C1001",
    "name": "",
    "city": "Irbid",
    "signup_date": datetime(2024, 3, 1)
})

customers.append({
    "customer_id": "C1002",
    "name": "Bad Date Customer",
    "city": "Zarqa",
    "signup_date": "not-a-date"
})

customers.append({
    "customer_id": "C001",
    "name": "Duplicate Customer",
    "city": "Aqaba",
    "signup_date": datetime(2024, 4, 1)
})

#Add messy data to products
products_data.append(
    ("P021", "Broken Product", "Electronics", -100)
)

products_data.append(
    ("P022", "", "Furniture", 50)
)

products_data.append(
    ("P001", "Duplicate Laptop", "Electronics", 900)
)

# Create DataFrames
customers_df = pd.DataFrame(customers)

products_df = pd.DataFrame(
    products_data,
    columns=["product_id", "product_name", "category", "price"]
)



# Create Sales
sales = []

for i in range (1, 10001):
    sale_id = f"S{i:05}"
    customer_id = random.choice(customers_df["customer_id"])
    product_id = random.choice(products_df["product_id"])
    quantity = random.randint(1,5)
    sale_date = datetime(2025, 1, 1) + timedelta(days = random.randint(0, 364))

    sale = {
        "sale_id": sale_id,
        "customer_id": customer_id,
        "product_id": product_id,
        "quantity": quantity,
        "sale_date": sale_date
    }
    sales.append(sale)

    
#Add messy data to sales
sales.append({
    "sale_id": "S99999",
    "customer_id": "C99999",
    "product_id": "P001",
    "quantity": 2,
    "sale_date": datetime(2025, 1, 1)
})

sales.append({
    "sale_id": "S99998",
    "customer_id": "C001",
    "product_id": "P99999",
    "quantity": 2,
    "sale_date": datetime(2025, 1, 1)
})

sales.append({
    "sale_id": "S99997",
    "customer_id": "C001",
    "product_id": "P001",
    "quantity": -5,
    "sale_date": datetime(2025, 1, 1)
})

sales.append({
    "sale_id": "S00001",
    "customer_id": "C001",
    "product_id": "P001",
    "quantity": 1,
    "sale_date": datetime(2025, 1, 1)
})


# Create  Sales DataFrame
sales_df = pd.DataFrame(sales)

# Save CSV Files
customers_df.to_csv(RAW_DATA_PATH / "customers.csv", index=False)
products_df.to_csv(RAW_DATA_PATH / "products.csv", index=False)
sales_df.to_csv(RAW_DATA_PATH / "sales.csv", index=False)

