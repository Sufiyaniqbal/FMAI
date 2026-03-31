import pandas as pd 

def total_sales(df):
    return df["amount"].sum()

def sales_by_customer(df):
    return df.groupby("customer")["amount"].sum().to_dict()

def sales_by_month(df):
    df["date"] = pd.to_datetime(df["date"])
    return df.groupby(df["date"].dt.to_period("M"))["amount"].sum().to_dict()

def top_customers( df , n = 5):
    return df.groupby("customer")["amount"].sum().sort_values(ascending=False ).head(n).to_dict()

def average_invoice(df):
    return df["amount"].mean()

if __name__ == "__main__":
    from loader import load_csv
    csv_path = "../data/sales.csv"
    df = load_csv(csv_path)
    print("Total Sales:", total_sales(df))
    print("Sales by Customer:", sales_by_customer(df))
    print("Sales by Month:", sales_by_month(df))
    print("Top 5 Customers:", top_customers(df))
    print("Average Invoice:", average_invoice(df))
