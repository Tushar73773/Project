import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# File Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_FILE = os.path.join(BASE_DIR, "sales.db")


# ==========================================
# Load Data
# ==========================================

def load_data():
    conn = sqlite3.connect(DATABASE_FILE)

    df = pd.read_sql("SELECT * FROM sales", conn)

    conn.close()

    return df


# ==========================================
# Top 10 Products
# ==========================================

def top_products_chart(df):

    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10,6))
    product_sales.plot(kind="bar")

    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


# ==========================================
# Category Pie Chart
# ==========================================

def category_chart(df):

    category_sales = (
        df.groupby("Category")["Total_Sales"]
        .sum()
    )

    plt.figure(figsize=(7,7))

    plt.pie(
        category_sales,
        labels=category_sales.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Sales by Category")

    plt.show()


# ==========================================
# Region Sales
# ==========================================

def region_chart(df):

    region_sales = (
        df.groupby("Region")["Total_Sales"]
        .sum()
    )

    plt.figure(figsize=(8,5))

    region_sales.plot(kind="bar")

    plt.title("Sales by Region")

    plt.xlabel("Region")
    plt.ylabel("Revenue")

    plt.tight_layout()

    plt.show()


# ==========================================
# Monthly Sales Trend
# ==========================================

def monthly_sales_chart(df):

    df["Date"] = pd.to_datetime(df["Date"])

    df["Month"] = df["Date"].dt.to_period("M")

    monthly = (
        df.groupby("Month")["Total_Sales"]
        .sum()
    )

    plt.figure(figsize=(10,5))

    monthly.plot(marker="o")

    plt.title("Monthly Sales Trend")

    plt.xlabel("Month")
    plt.ylabel("Revenue")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


# ==========================================
# Main
# ==========================================

def main():

    df = load_data()

    print("Generating Charts...")

    top_products_chart(df)

    category_chart(df)

    region_chart(df)

    monthly_sales_chart(df)

    print("Charts Generated Successfully.")


if __name__ == "__main__":
    main()