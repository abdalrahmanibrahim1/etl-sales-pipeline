import pandas as pd

def transform_data(customers_df, products_df, sales_df):

    customers_df = customers_df.copy()
    products_df = products_df.copy()
    sales_df = sales_df.copy()

    #cleaning customers dataframe
    customers_df = customers_df.drop_duplicates(
        subset = ["customer_id"],
        keep = "first"
    )

    customers_df = customers_df.dropna(subset=["customer_id"])
    customers_df = customers_df.dropna(subset=["signup_date"])


    customers_df["name"] = customers_df["name"].fillna("Unknown")
    customers_df["name"] = customers_df["name"].replace("", "Unknown")


    customers_df["signup_date"] = pd.to_datetime(
    customers_df["signup_date"],
    errors="coerce"
    )
    customers_df = customers_df.dropna(subset=["signup_date"])
    

    #cleaning products dataframe
    products_df = products_df.drop_duplicates(
        subset = ["product_id"],
        keep = "first"
    )

    products_df["product_name"] = products_df["product_name"].fillna("Unknown")
    products_df["product_name"] = products_df["product_name"].replace("","Unknown")

    products_df["price"] = pd.to_numeric(
    products_df["price"],
    errors = "coerce"
    )
    products_df = products_df.dropna(subset =["price"])
    products_df = products_df[products_df["price"]>0]



    # cleaning sales dataframe
    sales_df = sales_df.drop_duplicates(
        subset = ["sale_id"],
        keep = "first"
    )

    sales_df["quantity"] = pd.to_numeric(
        sales_df["quantity"],
        errors = "coerce"
    )
    sales_df["sale_date"] = pd.to_datetime(
        sales_df["sale_date"],
        errors= "coerce"
    )

    sales_df = sales_df.dropna(
        subset = ["sale_id", "customer_id", "product_id", "quantity", "sale_date"]
    )

    sales_df = sales_df[sales_df["quantity"] > 0]



    sales_df = sales_df[sales_df["customer_id"].isin(customers_df["customer_id"])]
    sales_df = sales_df[sales_df["product_id"].isin(products_df["product_id"])]
    


    return customers_df, products_df, sales_df
    






if __name__ == "__main__":
    from extract import extract_data

    customers, products, sales = extract_data()

    clean_customers, clean_products, clean_sales = transform_data(
        customers,
        products,
        sales
    )

