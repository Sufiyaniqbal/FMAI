import json
import os
import matplotlib.pyplot as plt

with open("reports/summary.json") as f:
    summary = json.load(f)

# print(f"Total customer revenue: {summary['total_customers']}")
# print(f"Total revenue: {summary['total_revenue']}")
# print(f"Average revenue per customer: {summary['average_revenue_per_customer']}")

# print("\nTop customers")
top_customers = summary['top_5_customers']  
# for i, customer in enumerate(top_customers , 1):
#     print(f"{i}. {customer['Name']}: {customer['TotalRevenue']}")


top_total = sum(c['TotalRevenue'] for c in top_customers)
perecentage = (top_total/summary['total_revenue'])*100
# print(f"top {len(top_customers)} customers contribute {round(perecentage,2)}% of total revenue")

country_sorted = sorted(summary['revenue_by_country'],key=lambda x:x['TotalRevenue'], reverse=True)
# print("\nRevenue by country:")
# for i, c in enumerate(country_sorted, 1):
#     print(f"{i}. {c['Country']}: {c['TotalRevenue']}")

insights = {
    "total_customers": summary["total_customers"],
    "total_revenue": summary["total_revenue"],
    "average_revenue_per_customer": summary["average_revenue_per_customer"],
    "top_customers": top_customers,
    "top_customers_contribution_pct": round(perecentage, 2),
    "revenue_by_country": country_sorted
}

output_file = os.path.join("reports", "insights.json")
with open(output_file, "w") as f:
    json.dump(insights, f, indent=4)
    
print("Insights saved to insights.json successfully!")

with open(output_file) as f:
    insights = json.load(f)

names = [c['Name'] for c in insights['top_customers']]
revenues = [c['TotalRevenue'] for c in insights['top_customers']]

country = [c['Country'] for c in insights['revenue_by_country']]
country_revenue = [c['TotalRevenue'] for c in insights['revenue_by_country']]

plt.figure(figsize=(8,5))
plt.bar(country,country_revenue,color="Skyblue")
plt.title("revenue by country")
plt.xlabel("Conutry Name")
plt.ylabel("Revenue")
plt.show()

