import sqlite3
import pandas as pd
import os

# ==========================================
# File Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_FILE = os.path.join(BASE_DIR, "sales.csv")
DATABASE_FILE = os.path.join(BASE_DIR, "sales.db")

# ==========================================
# Create Database
# ==========================================

def create_database():
    try:
        # Check if CSV exists
        if not os.path.exists(CSV_FILE):
            print(f"Error: sales.csv not found!")
            print(f"Expected Location:\n{CSV_FILE}")
            return

        # Read CSV
        df = pd.read_csv(CSV_FILE)

        # Create Total Sales column
        df["Total_Sales"] = df["Quantity"] * df["Price"]

        # Connect to SQLite
        conn = sqlite3.connect(DATABASE_FILE)

        # Save data into SQLite
        df.to_sql("sales", conn, if_exists="replace", index=False)

        conn.commit()
        conn.close()

        print("=" * 50)
        print("Database Created Successfully")
        print(f"Database Name : sales.db")
        print(f"Records Imported : {len(df)}")
        print("=" * 50)

    except Exception as e:
        print("Error while creating database:")
        print(e)


# ==========================================
# Display First Five Records
# ==========================================

def show_sample_data():
    try:
        conn = sqlite3.connect(DATABASE_FILE)

        query = """
        SELECT *
        FROM sales
        LIMIT 5
        """

        df = pd.read_sql(query, conn)

        conn.close()

        print("\nFirst 5 Records\n")
        print(df)

    except Exception as e:
        print("Error reading database:")
        print(e)


# ==========================================
# Total Records
# ==========================================

def total_records():
    try:
        conn = sqlite3.connect(DATABASE_FILE)

        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM sales")

        total = cursor.fetchone()[0]

        conn.close()

        print(f"\nTotal Records in Database : {total}")

    except Exception as e:
        print(e)


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":
    create_database()
    show_sample_data()
    total_records()