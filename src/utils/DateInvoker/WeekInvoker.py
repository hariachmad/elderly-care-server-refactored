from langchain_core.prompts import PromptTemplate
import json
from datetime import datetime, timedelta


def week_invokerV2(llm_, text, intent):


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

Your task is to extract WEEK intent into structured JSON.

Output format:

{"type": "week", "modifier": "<this|next|last|none>", "amount": int}

Rules:
- Do NOT calculate actual dates
- Only extract meaning

Modifier Rules:
- "this week" → modifier = "this"
- "next week" → modifier = "next"
- "last week" → modifier = "last"
- If only "week" → modifier = "none"

Amount Rules:
- "next 2 weeks" → amount = 2
- "next week" → amount = 1
- If not specified → amount = 1
- Convert text numbers to integer (e.g., "two" → 2)

STRICT RULE:
- Do NOT infer modifier if not present
- Always return valid JSON

Examples:

Input: "this week"
Output:
{"type": "week", "modifier": "this", "amount": 1}

Input: "next week"
Output:
{"type": "week", "modifier": "next", "amount": 1}

Input: "next 2 weeks"
Output:
{"type": "week", "modifier": "next", "amount": 2}

Input: {text}
""", input_variables=["text"])

    prompt = prompt_.format(text=text)

    result = llm_.invoke(prompt)

    result_dict = json.loads(result.content.strip())

    print("extracted:", result_dict)

    result_date = resolve_week_from_llm(result_dict)

    print("result date week :", result_date)


def resolve_week_from_llm(data):
    now = datetime.now()
    today_idx = now.weekday()

    start_of_week = now - timedelta(days=today_idx)

    modifier = data["modifier"]
    amount = data.get("amount", 1)

    if modifier == "this":
        target_date = start_of_week

    elif modifier == "next":
        target_date = start_of_week + timedelta(weeks=amount)

    elif modifier == "last":
        target_date = start_of_week - timedelta(weeks=amount)

    else: 
        target_date = start_of_week

    iso = target_date.isocalendar()

    return {
        "year": iso[0],
        "week": iso[1]
    }