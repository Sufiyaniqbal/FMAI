import json
from openai import OpenAI

def generate_ai_report(insights: dict, api_key : str):
    client = OpenAI(api_key=api_key)

    insights_json = json.dumps(insights, indent=2)

    prompt = f"""
    You are a business analyst. Read the following data and generate a clear, human-readable report.
    Include key insights, top customers, revenue by month, and recommendations.

    Data:
    {insights_json}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7

    )
    
    report_text = response.choices[0].message.content
    return report_text