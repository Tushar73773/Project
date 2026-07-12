import pandas as pd
from analysis import (
    load_data,
    total_revenue,
    total_orders,
    average_order_value,
    best_selling_products,
    sales_by_category,
    sales_by_region,
    top_revenue_products,
    monthly_sales
)
from charts import main as show_charts


def show_data(df):
    print("\n========== SALES DATA ==========\n")
    print(df.head(20))


def search_product(df):
    product = input("\nEnter Product Name: ").strip().lower()

    result = df[df["Product"].str.lower() == product]

    if result.empty:
        print("\nNo product found.")
    else:
        print(result)


def export_report(df):
    df.to_csv("sales_report.csv", index=False)
    print("\nReport exported successfully as sales_report.csv")


def menu():
    df = load_data()

    while True:

        print("\n" + "=" * 55)
        print("        SALES DATA ANALYSIS SYSTEM")
        print("=" * 55)

        print("1. View Sales Data")
        print("2. Total Revenue")
        print("3. Total Orders")
        print("4. Average Order Value")
        print("5. Best Selling Products")
        print("6. Sales by Category")
        print("7. Sales by Region")
        print("8. Top Revenue Products")
        print("9. Monthly Sales")
        print("10. Show Charts")
        print("11. Search Product")
        print("12. Export Report")
        print("13. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_data(df)

        elif choice == "2":
            total_revenue(df)

        elif choice == "3":
            total_orders(df)

        elif choice == "4":
            average_order_value(df)

        elif choice == "5":
            best_selling_products(df)

        elif choice == "6":
            sales_by_category(df)

        elif choice == "7":
            sales_by_region(df)

        elif choice == "8":
            top_revenue_products(df)

        elif choice == "9":
            monthly_sales(df)

        elif choice == "10":
            show_charts()

        elif choice == "11":
            search_product(df)

        elif choice == "12":
            export_report(df)

        elif choice == "13":
            print("\nThank you for using the Sales Data Analysis System.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    menu()