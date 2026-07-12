import sqlite3
import pandas as pd
import os

# ==========================================
# File Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_FILE = os.path.join(BASE_DIR, "sales.db")

# ==========================================
# Load Data from Database
# ==========================================

def load_data():
    conn = sqlite3.connect(DATABASE_FILE)

    query = "SELECT * FROM sales"

    df = pd.read_sql(query, conn)

    conn.close()

    return df


# ==========================================
# Total Revenue
# ==========================================

def total_revenue(df):

    revenue = df["Total_Sales"].sum()

    print(f"\nTotal Revenue        : Rs. {revenue:,.2f}")


# ==========================================
# Total Orders
# ==========================================

def total_orders(df):

    orders = len(df)

    print(f"Total Orders         : {orders}")


# ==========================================
# Average Order Value
# ==========================================

def average_order_value(df):

    average = df["Total_Sales"].mean()

    print(f"Average Order Value  : Rs. {average:,.2f}")


# ==========================================
# Best Selling Products
# ==========================================

def best_selling_products(df):

    products = (
        df.groupby("Product")["Quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== Top 10 Best Selling Products ==========\n")
    print(products.head(10))


# ==========================================
# Sales by Category
# ==========================================

def sales_by_category(df):

    category = (
        df.groupby("Category")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== Sales by Category ==========\n")
    print(category)


# ==========================================
# Sales by Region
# ==========================================

def sales_by_region(df):

    region = (
        df.groupby("Region")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== Sales by Region ==========\n")
    print(region)


# ==========================================
# Top Revenue Products
# ==========================================

def top_revenue_products(df):

    revenue = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== Top Revenue Generating Products ==========\n")
    print(revenue.head(10))


# ==========================================
# Monthly Sales
# ==========================================

def monthly_sales(df):

    df["Date"] = pd.to_datetime(df["Date"])

    df["Month"] = df["Date"].dt.strftime("%B")

    monthly = (
        df.groupby("Month")["Total_Sales"]
        .sum()
    )

    print("\n========== Monthly Sales ==========\n")
    print(monthly)


# ==========================================
# Main Program
# ==========================================

def main():

    df = load_data()

    print("=" * 60)
    print("        SALES DATA ANALYSIS REPORT")
    print("=" * 60)

    total_revenue(df)
    total_orders(df)
    average_order_value(df)

    best_selling_products(df)
    sales_by_category(df)
    sales_by_region(df)
    top_revenue_products(df)
    monthly_sales(df)

    print("\n" + "=" * 60)
    print("Analysis Completed Successfully")
    print("=" * 60)


if __name__ == "__main__":
    main()