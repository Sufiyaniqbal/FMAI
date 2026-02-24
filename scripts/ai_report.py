import json
from config import OPENAI_API_KEY
from openai import OpenAI  # new v1.0+ API

# Create client
client = OpenAI(api_key=OPENAI_API_KEY)

# Load insights.json
with open("reports/insights.json") as f:
    insights = json.load(f)

# Prepare prompt
prompt = f"""
You are a business analyst. Read the following JSON data and generate a clear, human-readable report in short paragraphs.
Include key insights, top customers, revenue by country, and recommendations for the business.

JSON Data:
{insights}
"""

# Call AI
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # your available model
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)

# Extract text
report_text = response.choices[0].message.content

# Save report
with open("reports/ai_report.txt", "w") as f:
    f.write(report_text)

print("AI report generated successfully!")
print(report_text)