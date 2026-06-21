import sqlite3
from pathlib import Path
from transform import transform_data
from extract import extract_data

def load_data():
    # Creating path variables
    DATABASE_DIR = Path("database")
    DATABASE_DIR.mkdir(exist_ok=True)
    DATABASE_PATH = DATABASE_DIR / "sales_pipeline.db"

    #Loading in clean dataframes
    customers, products, sales = extract_data()
    customers, products, sales = transform_data(customers, products, sales)

    #converting pandas date object to string
    customers["signup_date"] = customers["signup_date"].astype(str)
    sales["sale_date"] = sales["sale_date"].astype(str)

    #creating database connection
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    #Creating tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            customer_id TEXT PRIMARY KEY NOT NULL,
            name TEXT,
            city TEXT,
            signup_date TEXT
        )
    """
    )

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            product_id TEXT PRIMARY KEY NOT NULL,
            product_name TEXT,
            category TEXT,
            price REAL
        )
    """
    )
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            sale_id TEXT PRIMARY KEY NOT NULL,
            customer_id TEXT,
            product_id TEXT,
            quantity INT,
            sale_date TEXT,
                   
            FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY(product_id) REFERENCES products(product_id)
        )
    """
    )

    #Emptying tables
    cursor.execute("DELETE FROM sales")
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM customers")

    #Inserting dataframes into db tables
    cursor.executemany(
        """
        INSERT INTO customers (customer_id, name, city, signup_date)
        VALUES (?, ?, ?, ?)
        """, customers.values.tolist()
    )

    cursor.executemany(
        """
        INSERT INTO products (product_id, product_name, category, price)
        VALUES (?, ?, ?, ?)
        """, products.values.tolist()
    )
    cursor.executemany(
        """
        INSERT INTO sales (sale_id, customer_id, product_id, quantity, sale_date)
        VALUES (?, ?, ?, ?, ?)
        """, sales.values.tolist()
    )

    conn.commit()
    conn.close()
    print("Data loaded successfully.")

if __name__ == "__main__":
    load_data()