import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    cust_ord = customers.merge(orders, left_on= "id", right_on="customerId", how="left")

    cust_ord.rename(columns={"name":"Customers"},inplace=True)
    return cust_ord[cust_ord["customerId"].isna()][["Customers"]]