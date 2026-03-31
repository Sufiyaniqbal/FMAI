from loader import load_csv
from analyzer import sales_by_customer,sales_by_month,total_sales,top_customers,average_invoice

csv_path  = "../data/sales.csv"
df = load_csv(csv_path)

prompt_map = {
    "total sales": total_sales,
    "sales by customer": sales_by_customer,
    "sales by month": sales_by_month,
    "top customers": top_customers,
    "average invoice": average_invoice
}

user_prompt = input("Enter your request: ").lower()

mathed_func = None
for key in prompt_map:
    if key in user_prompt:
        mathed_func = prompt_map[key]
        break

if mathed_func:
    if mathed_func == "total_sales":    
        result = mathed_func(df, n=5)
    else:
        result = mathed_func(df)
    print("\n=== Report ===")
    print(result)
else:
    print("Sorry, I didn't understand the request. Try one of these:")
    for key in prompt_map:
        print("-", key)
    