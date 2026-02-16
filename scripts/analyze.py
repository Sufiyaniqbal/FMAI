import pandas as pd
import os

data_folder = '../data'
report_folder = '../reports'

os.makedirs(report_folder,exist_ok=True)

customers = pd.read_csv(os.path.join(data_folder,'customers.csv'))
invoices = pd.read_csv(os.path.join(data_folder,'invoices.csv'))

total_customers = customers.shape[0]
total_invoices = invoices.shape[0]
total_revenue = invoices['Amount'].sum()

revenue_per_customer = invoices.groupby('CustomerID')['Amount'].sum()

customer_report = customers.merge(revenue_per_customer.reset_index(), left_on='CustomerID', right_on='CustomerID', how='left')
customer_report.rename(columns={'Amount': 'TotalRevenue'}, inplace=True)

report_file = os.path.join(report_folder,'customer_report.csv')
customer_report.to_csv(report_file,index=False)

print("----- Business Summary -----")
print(f"Total Customers: {total_customers}")
print(f"Total Invoices: {total_invoices}")
print(f"Total Revenue: {total_revenue}")

top_customer_id = revenue_per_customer.idxmax()
top_customer_name = customers.loc[customers['CustomerID'] == top_customer_id, 'Name'].values[0]
top_customer_revenue = revenue_per_customer.max()

print("\nTop Customer:")
print(f"ID: {top_customer_id}")
print(f"Name: {top_customer_name}")
print(f"Revenue: {top_customer_revenue}")

print(f"\nReport saved to: {report_file}")