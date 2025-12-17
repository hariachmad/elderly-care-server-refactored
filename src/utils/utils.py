from datetime import datetime
from langchain_core.prompts import PromptTemplate
import dateparser
import re
import string

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
    if dt is None:
        return {}    
    if dt.date is None:
        dt_query = {
        'date' : dt.date().isoformat(),
        'time' : None if dt.time() == datetime.min.time() else dt.time().isoformat()
        }
        return dt_query
    return {}

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