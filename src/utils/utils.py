from datetime import datetime
from langchain_core.prompts import PromptTemplate
import dateparser
import re

def date_time_invoker(llm_, text):
    prompt_ = PromptTemplate(template=
    """
        Extract the date and time from the following text.
        - Always answer only in ISO format.
        - If both date and time are found → return YYYY-MM-DDTHH:MM:SS
        - If date exists but time is missing → return YYYY-MM-DD (without time part)
        - If no date is found → use today's date ({today})
        - If no time is found → default to 00:00
        - If year is missing → use the current year ({year})

        Input: {text}
        """
        )
    now = datetime.now()
    today_iso = now.strftime("%Y-%m-%d")
    current_year = now.strftime("%Y")
    
    prompt : PromptTemplate = prompt_
    prompt = prompt.format(text=text, today=today_iso, year=current_year)

    result = llm_.invoke(prompt)
    dt = dateparser.parse(result.content.strip())
    dt_query = {
    'date' : dt.date().isoformat(),
    'time' : None if dt.time() == datetime.min.time() else dt.time().isoformat()
    }
    return dt_query

def blacklist_keyword_guard(blacklist_keywords, text)-> bool:
    pattern = re.compile(r"(" + "|".join(map(re.escape, blacklist_keywords)) + r")", re.IGNORECASE)
    return bool(pattern.search(text))