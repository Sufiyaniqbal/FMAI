# scripts/ai_router.py
from openai import OpenAI
from analyzer import total_sales, sales_by_customer, sales_by_month, top_customers, average_invoice
from config import OPENAI_API_KEY

# Initialize client (use your API key)
client = OpenAI(api_key=OPENAI_API_KEY)

# Function metadata for AI
functions = [
    {"name": "total_sales", "description": "Calculate total sales amount"},
    {"name": "sales_by_customer", "description": "Show total sales grouped by each customer"},
    {"name": "sales_by_month", "description": "Show total sales grouped by month"},
    {"name": "top_customers", "description": "Get top 5 customers by total sales"},
    {"name": "average_invoice", "description": "Calculate the average invoice amount"}
]

# Map function names to Python functions
function_map = {
    "total_sales": total_sales,
    "sales_by_customer": sales_by_customer,
    "sales_by_month": sales_by_month,
    "top_customers": top_customers,
    "average_invoice": average_invoice
}

# Function to let AI decide which Python function to call
def decide_function(user_prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant that selects the correct function from the given metadata based on the user prompt."},
            {"role": "user", "content": user_prompt}
        ],
        functions=functions,
        function_call="auto"
    )

    message = response.choices[0].message

    if message.function_call:
        return message.function_call.name
    return None

# Optional: function to rephrase raw results
def rephrase_result(user_prompt, raw_result):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a business analyst. Rephrase the raw result into a short, clear, human-readable report."},
            {"role": "user", "content": f"User request: {user_prompt}\nRaw result: {raw_result}"}
        ]
    )
    return response.choices[0].message.content