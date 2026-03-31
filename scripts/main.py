# from loader import load_csv
# from analyzer import top_customers,total_sales,sales_by_customer,sales_by_month,average_invoice
# from config import OPENAI_API_KEY
# from report_generator import generate_ai_report

# csv_path = "../data/sales.csv"
# df = load_csv(csv_path)

# prompt_map = {
#     "total sales": total_sales,
#     "sales by customer": sales_by_customer,
#     "sales by month": sales_by_month,
#     "top customers": top_customers,
#     "average invoice": average_invoice
# }

# user_prompt = input("Enter your request :").lower()

# matched_func = None
# for key in prompt_map:
#     if key in user_prompt:
#         matched_func = prompt_map[key]
#         break

# if not matched_func:
#     print("❌ Sorry, I didn't understand.")
#     exit()

# if matched_func == top_customers:
#     result = matched_func(df , n=5)
# else:
#     result = matched_func(df)

# insights = {
#     "user_request": user_prompt,
#     "result": result
# }

# try:
#     report = generate_ai_report(insights, api_key=OPENAI_API_KEY)
# except Exception as e:
#     print("⚠️ AI not available, showing raw result.")
#     report = str(result)

# with open("../reports/ai_report.txt", "w") as f:
#     f.write(report)

# print(report)

from loader import load_csv
from ai_router import decide_function, function_map, rephrase_result

# Load CSV
df = load_csv("../data/sales.csv")

# Get user prompt
user_prompt = input("Ask your question: ")

# AI decides which function to run
func_name = decide_function(user_prompt)

if func_name in function_map:
    # Run the selected function
    raw_result = function_map[func_name](df)
    print("Raw result:", raw_result)

    # Optional: rephrase using AI
    final_report = rephrase_result(user_prompt, raw_result)
    print("\nAI Report:\n", final_report)
else:
    print("Sorry, I didn't understand your request.")
            