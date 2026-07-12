import pandas as pd
import random
from datetime import datetime, timedelta

# -------------------------------
# Configuration
# -------------------------------
NUM_RECORDS = 800

products = {
    "Laptop": ("Electronics", 55000, 70000),
    "Mouse": ("Accessories", 300, 800),
    "Keyboard": ("Accessories", 800, 2500),
    "Monitor": ("Electronics", 12000, 25000),
    "Printer": ("Electronics", 9000, 18000),
    "Headphones": ("Accessories", 1000, 5000),
    "USB Cable": ("Accessories", 150, 500),
    "SSD": ("Electronics", 2500, 8000),
    "Webcam": ("Electronics", 1500, 6000),
    "Speaker": ("Accessories", 1200, 5000),
    "Power Bank": ("Accessories", 800, 3500),
    "Smart Watch": ("Electronics", 3000, 12000),
    "Router": ("Electronics", 1800, 7000),
    "Pendrive": ("Accessories", 400, 1800),
    "Microphone": ("Electronics", 2000, 9000)
}

regions = ["North", "South", "East", "West"]

start_date = datetime(2025, 1, 1)

sales_data = []

for order_id in range(1001, 1001 + NUM_RECORDS):

    product = random.choice(list(products.keys()))
    category, min_price, max_price = products[product]

    price = random.randint(min_price, max_price)
    quantity = random.randint(1, 8)

    date = start_date + timedelta(days=random.randint(0, 364))

    region = random.choice(regions)

    sales_data.append({
        "Order_ID": order_id,
        "Date": date.strftime("%Y-%m-%d"),
        "Product": product,
        "Category": category,
        "Region": region,
        "Quantity": quantity,
        "Price": price
    })

df = pd.DataFrame(sales_data)

df.to_csv("sales.csv", index=False)

print("sales.csv generated successfully!")
print("Total Records:", len(df))