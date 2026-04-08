from langchain_core.prompts import PromptTemplate
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta


def month_invokerV2(llm_, text, intent):

    prompt_ = PromptTemplate(template=
    """
You MUST return ONLY valid JSON.

DO NOT include:
- explanations
- any text outside JSON
- markdown (no ```)

Output must be a SINGLE JSON object and must be parseable by JSON.parse().

If your output is invalid JSON, fix it before responding.

---

Your task is to extract MONTH intent into structured JSON.

Output format:

{{"type": "month", "modifier": "<this|next|last|none>", "amount": int, "month_number": int|null, "year": int|null}}

Rules:
- Do NOT calculate actual dates
- Only extract meaning

Modifier Rules:
- "this month" → modifier = "this"
- "next month" → modifier = "next"
- "last month" → modifier = "last"
- If only "month" → modifier = "none"

Month Number Rules:
- "month 5" → month_number = 5
- "in month 12" → month_number = 12
- "January" → month_number = 1
- "Feb" → month_number = 2
- If month_number exists → modifier MUST be "none"

Amount Rules:
- "next 2 months" → amount = 2
- "next month" → amount = 1
- If not specified → amount = 1

STRICT RULE:
- If month_number is present → ignore modifier & amount logic (set amount = 1)
- Do NOT infer modifier if not present
- Always return valid JSON
Year Rules:
- If year is mentioned → extract it
- If not → year = null

Examples:

Input: "this month"
Output:
{{"type": "month", "modifier": "this", "amount": 1, "month_number": null}}

Input: "next 2 months"
Output:
{{"type": "month", "modifier": "next", "amount": 2, "month_number": null}}

Input: "month 5"
Output:
{{"type": "month", "modifier": "none", "amount": 1, "month_number": 5}}

Input: "January"
Output:
{{"type": "month", "modifier": "none", "amount": 1, "month_number": 1}}

Input: {text}
""", input_variables=["text"])

    prompt = prompt_.format(text=text)

    result = llm_.invoke(prompt)

    result_dict = json.loads(result.content.strip())

    print("extracted:", result_dict)

    result_date_json = resolve_month_from_llm(result_dict)

    print("result date month :", result_date_json)

    return result_date_json

def resolve_month_from_llm(data):
    now = datetime.now()

    modifier = data.get("modifier")
    amount = data.get("amount", 1)
    month_number = data.get("month_number")
    year = data.get("year")
    target_date = None

    if month_number is not None:
        month_number = int(month_number)

        if year is not None:
            return {
                "year": int(year),
                "month": month_number
            }

        if month_number < now.month:
            resolved_year = now.year + 1
        else:
            resolved_year = now.year

        return {
            "year": resolved_year,
            "month": month_number
        }

    if modifier == "this":
        target_date = now

    elif modifier == "next":
        target_date = now + relativedelta(months=amount)

    elif modifier == "last":
        target_date = now - relativedelta(months=amount)

    else:
        target_date = now

    return {
        "year": target_date.year,
        "month": target_date.month
    }