import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")


def extract_data():
    customers_df = pd.read_csv(RAW_DATA_PATH / "customers.csv")
    products_df = pd.read_csv(RAW_DATA_PATH / "products.csv")
    sales_df = pd.read_csv(RAW_DATA_PATH / "sales.csv")

    return customers_df, products_df, sales_df

if __name__ == "__main__":
    customers, products, sales = extract_data()

    print(customers.shape)
    print(products.shape)
    print(sales.shape)