import sqlite3
from pathlib import Path

DATABASE_PATH = Path("database/sales_pipeline.db")


def best_selling_product():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.product_name, SUM(s.quantity) AS total_units_sold
        FROM sales AS s
        JOIN products AS p
        ON s.product_id = p.product_id
        GROUP BY p.product_id,p.product_name
        ORDER BY total_units_sold DESC
        LIMIT 1
    """)
    result = cursor.fetchone()
    print(f"The best selling product is: {result[0]} ({result[1]} units sold)")
    conn.close()


def top_product_by_revenue():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.product_name, SUM(s.quantity * p.price) AS total_revenue
        FROM sales AS s
        JOIN products AS p
        ON s.product_id = p.product_id
        GROUP BY p.product_id,p.product_name
        ORDER BY total_revenue DESC
        LIMIT 1
    """)

    result = cursor.fetchone()
    print(f"The top product by revenue: {result[0]} (${result[1]:,.0f} total revenue)")
    conn.close()

def sales_by_city():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.city, SUM(s.quantity * p.price) AS total_revenue
        FROM sales AS s
        JOIN products AS p
        ON s.product_id = p.product_id
        JOIN customers as c
        ON s.customer_id = c.customer_id
        GROUP BY c.city
        ORDER BY total_revenue DESC
    """)

    result = cursor.fetchall()

    print(f"{'City':<10} {'Revenue':<15}")
    for city, revenue in result:
        formatted_revenue = f"${revenue:,.0f}"
        print(f"{city:<10} {formatted_revenue:<15}")

    conn.close()

def revenue_by_category():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.category, SUM(s.quantity * p.price) AS total_revenue
        FROM sales AS s
        JOIN products AS p
        ON s.product_id = p.product_id
        GROUP BY p.category
        ORDER BY total_revenue DESC
    """)

    result = cursor.fetchall()

    print(f"{'Category':<13} {'Revenue':<15}")
    for category, revenue in result:
        formatted_revenue = f"${revenue:,.0f}"
        print(f"{category:<13} {formatted_revenue:<15}")

    conn.close()

def monthly_sales_trend():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT strftime('%Y-%m',s.sale_date) AS month, SUM(s.quantity * p.price) AS total_revenue
        FROM sales AS s
        JOIN products AS p
        ON s.product_id = p.product_id
        GROUP BY month
        ORDER BY month ASC
    """)

    result = cursor.fetchall()

    print(f"{'Month':<10} {'Revenue':<15}")
    for month, revenue in result:
        formatted_revenue = f"${revenue:,.0f}"
        print(f"{month:<10} {formatted_revenue:<14}")

    conn.close()

def top_customer_by_spending():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.name, SUM(s.quantity * p.price) AS total_revenue
        FROM sales AS s
        JOIN products AS p
        ON s.product_id = p.product_id
        JOIN customers as c
        ON s.customer_id = c.customer_id
        GROUP BY c.customer_id, c.name
        ORDER BY total_revenue DESC
        LIMIT 1
    """)

    result = cursor.fetchone()
    name, revenue = result

    print(
        f"Top spending customer is {name} "
        f"with a total of ${revenue:,.0f} spent"
    )
    conn.close()    


if __name__ == "__main__":
    best_selling_product()
    top_product_by_revenue()
    sales_by_city()
    revenue_by_category()
    monthly_sales_trend()
    top_customer_by_spending()

