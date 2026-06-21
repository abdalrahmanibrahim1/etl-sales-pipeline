from load import load_data
from report import (
    best_selling_product,
    top_product_by_revenue,
    sales_by_city,
    monthly_sales_trend,
    top_customer_by_spending
)

def main():
    load_data()

    best_selling_product()
    top_product_by_revenue()
    sales_by_city()
    monthly_sales_trend()
    top_customer_by_spending()

if __name__ == "__main__":
    main()