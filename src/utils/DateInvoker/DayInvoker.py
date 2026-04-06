from langchain_core.prompts import PromptTemplate
from datetime import datetime, timedelta
import json

today = datetime.now()
year = today.year
month = today.strftime("%B")
day = today.day

days_map = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}   

def day_invokerV2(llm_, text, intent):
    prompt_ = PromptTemplate(template=
    """
        Your task is NOT to calculate the final date.

        Your task is to extract the date intent into structured JSON.

        You MUST return ONLY valid JSON.

        DO NOT include:
        - explanations
        - any text outside JSON
        - markdown (no ```)

        Output must be a SINGLE JSON object and must be parseable by JSON.parse().

        If your output is invalid JSON, fix it before responding.

        ---

        Your task is NOT to calculate the final date.
        Your task is to extract the date intent into structured JSON.

        Output format:

        - weekday:
          {{"type": "weekday", "value": "<day>", "modifier": "<this|next|last|none>"}}

        - specific date:
          {{"type": "date", "year": int, "month": int, "day": int}}

        - relative:
          {{"type": "relative", "value": "today|tomorrow|yesterday"}}

        - relative range:
        {{"type": "relative_range", "value": "day", "amount": int, "direction": "future|past"}}

        Rules:
        - Do NOT calculate actual calendar dates
        - Do NOT guess the final date
        - Only extract structured meaning

        Modifier Rules:
- Only use "this", "next", or "last" IF the user explicitly mentions it.
- If the user only says a day (e.g., "Sunday"), you MUST use "none".
- Do NOT infer or assume "next" or "this" if it is not clearly stated.

        STRICT RULE:
- Never add a modifier that does not exist in the user input.
- If no modifier word is present, the modifier MUST be "none".

    Examples:

Input: "sunday"
Output: 
{{"type": "weekday", "value": "sunday", "modifier": "none"}}

Input: "appointment on sunday"
Output:
{{"type": "weekday", "value": "sunday", "modifier": "none"}}

Input: "next sunday"
Output:
{{"type": "weekday", "value": "sunday", "modifier": "next"}}

        Input: {text}
        """, input_variables=["text"],
        )
    
    prompt : PromptTemplate = prompt_
    # prompt = prompt.format(text=text, today=today_iso, year=current_year)
    prompt = prompt.format(text=text)

    result = llm_.invoke(prompt)
    result : dict= json.loads(result.content.strip())
    print("extracted: ", resolve_date_from_llm(result))
    result_date :datetime | None =resolve_date_from_llm(result)
    result_date_json = datetime_to_json(result_date)
    print("result date json: ", result_date_json)
    return result_date_json

def resolve_weekday(value: str, modifier: str):
    today = datetime.now()
    today_idx = today.weekday()  # Monday=0

    target_idx = days_map[value]

    if modifier == "none":
        delta = (target_idx - today_idx + 7) % 7
        if delta == 0:
            delta = 7

    elif modifier == "this":
        start_of_week = today - timedelta(days=today_idx)
        result = start_of_week + timedelta(days=target_idx)
        return result

    elif modifier == "next":
        delta = (target_idx - today_idx + 7) % 7
        if delta == 0:
            delta = 7
        delta += 7

    elif modifier == "last":
        delta = (target_idx - today_idx - 7) % 7
        delta -= 7

    else:
        raise ValueError("Invalid modifier")

    return today + timedelta(days=delta)

def resolve_relative(value: str):
    today = datetime.now()

    if value == "today":
        return today
    elif value == "tomorrow":
        return today + timedelta(days=1)
    elif value == "yesterday":
        return today - timedelta(days=1)

def resolve_date(year, month, day):
    today = datetime.now()

    return datetime(
        year or today.year,
        month or today.month,
        day
    )

def resolve_relative_range(amount: int, direction: str):
    now = datetime.now()

    if direction == "future":
        return now + timedelta(days=amount)

    elif direction == "past":
        return now - timedelta(days=amount)

    else:
        raise ValueError("Invalid direction")

def resolve_date_from_llm(data):
    if data["type"] == "weekday":
        return resolve_weekday(data["value"], data["modifier"])

    elif data["type"] == "relative":
        return resolve_relative(data["value"])

    elif data["type"] == "date":
        return resolve_date(
            data.get("year"),
            data.get("month"),
            data.get("day")
        )
    elif data["type"] == "relative_range":
        return resolve_relative_range(data["amount"], data["direction"])

    else:
        raise ValueError("Unknown type")

def datetime_to_json(dt: datetime) -> dict:
    return {
        "year": dt.year,
        "month": dt.month,
        "day": dt.day
    }