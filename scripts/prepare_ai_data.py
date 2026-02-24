import pandas as pd
import json
import os

# File paths
base_path = os.path.dirname(os.path.dirname(__file__))
reports_path = os.path.join(base_path, "reports")

customer_file = os.path.join(reports_path, "customer_report.csv")
top5_file = os.path.join(reports_path, "top_5_customers.csv")
country_file = os.path.join(reports_path, "revenue_by_country.csv")
no_revenue_file = os.path.join(reports_path, "no_revenue_customer.csv")

# Load data
customer_df = pd.read_csv(customer_file)
top5_df = pd.read_csv(top5_file)
country_df = pd.read_csv(country_file)
no_revenue_df = pd.read_csv(no_revenue_file)

# Create summary dictionary
summary = {
    "total_customers": len(customer_df),
    "total_revenue": float(customer_df["TotalRevenue"].sum()),
    "average_revenue_per_customer":float(customer_df["TotalRevenue"].mean()),
    "top_5_customers": top5_df.to_dict(orient="records"),
    "revenue_by_country": country_df.to_dict(orient="records"),
    "customers_without_revenue": no_revenue_df.to_dict(orient="records")
}

# Save as JSON
output_file = os.path.join(reports_path, "summary.json")

with open(output_file, "w") as f:
    json.dump(summary, f, indent=4)

print("AI summary file created successfully!")