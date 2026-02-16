import pandas as pd

customers = pd.read_csv('../data/customers.csv')
invoices = pd.read_csv('../data/invoices.csv')

total_customers = customers.shape[0]
total_invoices = invoices.shape[0]
total_revenue = invoices['Amount'].sum()

print("----- Business Summary -----")
print(f"Total Customers: {total_customers}")
print(f"Total Invoices: {total_invoices}")
print(f"Total Revenue: {total_revenue}")


revenue_per_customer = invoices.groupby('CustomerID')['Amount'].sum()

top_customer_id = revenue_per_customer.idxmax()
top_customer_revenue = revenue_per_customer.max()

print("\nTop Customer ID:", top_customer_id)
print("Top Customer Revenue:", top_customer_revenue)