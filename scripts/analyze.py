import pandas as pd

customers = pd.read_csv('../data/customers.csv')
invoices = pd.read_csv('../data/invoices.csv')

print("Customers:")
print(customers.head())

print("Invoices:")
print(invoices.head())