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

customer_report = customers.merge(revenue_per_customer.reset_index(), on='CustomerID', how='left').rename(columns={'Amount': 'TotalRevenue'})

main_report_file = os.path.join(report_folder,'customer_report.csv')
customer_report.to_csv(main_report_file,index=False)

top_n = 5
top_customers = customer_report.nlargest(top_n,'TotalRevenue')
print(top_customers)
top_customers_file = os.path.join(report_folder,f'top_{top_n}_customers.csv')
top_customers.to_csv(top_customers_file,index=False)

revenue_by_country = customer_report.groupby('Country')['TotalRevenue'].sum().reset_index()
country_report_file = os.path.join(report_folder,'revenue_by_country.csv')
revenue_by_country.to_csv(country_report_file,index=False)

no_revenue_customer = customer_report[customer_report['TotalRevenue'].isna()]
no_revenue_file = os.path.join(report_folder,'no_revenue_customer.csv')
no_revenue_customer.to_csv(no_revenue_file,index=False)

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

print("\nReports saved:")
print(f"- Main Customer Report: {main_report_file}")
print(f"- Top {top_n} Customers: {top_customers_file}")
print(f"- Revenue by Country: {country_report_file}")
print(f"- Customers with No Revenue: {no_revenue_file}")