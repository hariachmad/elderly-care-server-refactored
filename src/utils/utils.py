from datetime import datetime
from langchain_core.prompts import PromptTemplate
import dateparser
import re
import string
import json

today = datetime.now()
year = today.year
month = today.strftime("%B")
day = today.day

def date_time_invoker(llm_, text, intent):
    if "weekly" in intent.lower():
        return week_invoker(llm_, text)
    if "monthly" in intent.lower():
        return month_invoker(llm_, text)
    if "day" in intent.lower():
        return day_invoker(llm_, text)

def day_invoker(llm_, text):
    prompt_ = PromptTemplate(template=
    """
        System time is : {today}

        Your task is to extract the date from the user's request regarding a schedule. The output MUST be a JSON object in the following format:
{{"year": <int>, "month": <int>, "day": <int>}}.

Rules:

1. If the user asks for "today": Use the current system date.

2. If the user mentions a specific date (e.g., "January 05"): Convert the month name into its numeric value.

3. If the year is not mentioned, use the current system year.

4. If the user only mentions a day number (e.g., "the 30th"): Use the current system month and year.

5. If the user mentions a day of the week (e.g., "Monday"): Find the nearest upcoming date after today that matches that day.

Output only the JSON; do not include any additional text.

        Input: {text}
        """, input_variables=["text", "today", "year", "month", "day"],
        )
    
    prompt : PromptTemplate = prompt_
    # prompt = prompt.format(text=text, today=today_iso, year=current_year)
    prompt = prompt.format(text=text, today=today, year=year, month=month, day=day)

    result = llm_.invoke(prompt)
    print(result.content.strip())
    result : dict= json.loads(result.content.strip()) 
    return result

def week_invoker(llm_, text):
    prompt_ = PromptTemplate(template=
    """
Your task is to extract week information from the user's request regarding a schedule. The output MUST be a JSON object in the following format: {{"year": <int>, "week": <int>}}.

Today is : {today}

Rules:

1. If the user asks for "this week":

Use the current system date.

Convert the system date to its corresponding week number of the year (use the ISO week standard).

2. If the user mentions "Week <number>":

If the year is not mentioned, use the current system year.

3. If the user mentions "next week":

Use the current system date.

If the week number exceeds 52, reset to 1 and increment the year.

4. Output only the JSON; do not include any additional text.


        Input: {text}
        """, input_variables=["text", "today", "year", "month", "day"],
        )
    
    prompt : PromptTemplate = prompt_
    # prompt = prompt.format(text=text, today=today_iso, year=current_year)
    prompt = prompt.format(text=text, today=today, year=year, month=month, day=day)

    result = llm_.invoke(prompt)
    print(result.content.strip())
    result : dict= json.loads(result.content.strip()) 
    return result

def month_invoker(llm_, text):
    prompt_ = PromptTemplate(template=
    """
Your task is to extract month and year information from the user's request about schedules.
The output MUST be JSON in the format {{"year": <int>, "month": <int>}}.

Today is: {today}

Rules:
1. If the user asks for "this month":
   - Use the system date.
   - Convert the system date into its month number and year.
2. If the user specifies a month and year (e.g., "February 2027"):
   - Convert the month name into its numeric value.
   - Use the provided year.
3. If the user specifies only a month name (e.g., "February"):
   - Convert the month name into its numeric value.
   - If the year is missing, use the system year.
4. If the user asks for "next month":
   - Use the system date.
   - If the month exceeds 12, reset to 1 and increment the year.
5. Output ONLY the JSON, no extra text.


        Input: {text}
        """, input_variables=["text", "today", "year", "month", "day"],
        )
    
    prompt : PromptTemplate = prompt_
    # prompt = prompt.format(text=text, today=today_iso, year=current_year)
    prompt = prompt.format(text=text, today=today, year=year, month=month, day=day)

    result = llm_.invoke(prompt)
    result : dict= json.loads(result.content.strip()) 
    return result

def blacklist_keyword_guard(blacklist_keywords, text)-> bool:
    pattern = re.compile(r"(" + "|".join(map(re.escape, blacklist_keywords)) + r")", re.IGNORECASE)
    return bool(pattern.search(text))

def wake_word_guard(wake_word, text)-> bool:
    print("wake word text: ", text['user_input'])
    text_clean = text['user_input'].translate(str.maketrans("", "", string.punctuation))
    pattern = re.compile(r"(" + "|".join(map(re.escape, wake_word)) + r")", re.IGNORECASE)
    return bool(pattern.search(text_clean))

def clean_for_tts(text):
    text = re.sub(r"[^\w\s.,!?]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def generate_node_name(intent: str):
    return intent.replace(" ", "_")