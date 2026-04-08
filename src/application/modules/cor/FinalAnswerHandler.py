from application.modules.cor.Handler import Handler
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from infrastructure.LlmClient import LlmClient

class FinalAnswerHandler(Handler):
    def handle(self,input, lang="en", additional_answer=""):
        load_dotenv()
        prompt_template = PromptTemplate(
template="""
You are a response generator for a robot assistant.

Your task is to generate a final answer label based on the time reference in the user input.

---

OUTPUT RULES:
- Return ONLY plain text
- DO NOT return JSON
- DO NOT add explanation
- Output MUST be ONE of the following EXACT values OR empty:

today
tomorrow
yesterday
specific_date
specific_week
this_week
next_week
last_week
specific_month
this_month
next_month
last_month

- If NO time reference is found → return EMPTY STRING ("")
- DO NOT guess
- DO NOT infer missing time information

---

CLASSIFICATION RULES:

1. RELATIVE DAY:
- "today" → today
- "tomorrow" → tomorrow
- "yesterday" → yesterday

2. SPECIFIC DATE:
- If user mentions a specific calendar date
  (e.g., March 12, 12th, tanggal 5, Jan 20)
→ return: specific_date

3. WEEK:
- "this week" → this week
- "next week" → next week
- "last week" → last week
- If user mentions week number (week 18, minggu ke-18)
→ return: specific_week

4. MONTH:
- "this month" → this month
- "next month" → next month
- "last month" → last month
- If user mentions a specific month (May, January, Maret)
→ return: specific_month

---

IMPORTANT:
- DO NOT output actual values like "March 12" or "week 18"
- ALWAYS map to the abstract label
- Choose the MOST specific match
- If there is NO clear time reference → return ""

---

Examples:

User: "Show my schedule today"
Answer: today

User: "Show my schedule tomorrow"
Answer: tomorrow

User: "Show my scheduled medication for March 12"
Answer: specific_date

User: "Show my schedule for week 18"
Answer: specific_week

User: "Show my schedule this week"
Answer: this_week

User: "Show my schedule for May"
Answer: specific_month

User: "Show my schedule this month"
Answer: this_month

User: "Show my schedule"
Answer: ""

User: "Hello robot"
Answer: ""

---

User input:
{text}

Answer:
""",
input_variables=["text"]
)
        prompt : PromptTemplate = prompt_template.format(text=input)
        model = os.getenv("LLM_MODEL")
        temperature = int(os.getenv("LLM_TEMPERATURE", "0"))
        base_url = os.getenv("LLM_BASE_URL", "http://localhost:11434/")
        llm = LlmClient(model, temperature, base_url).instance
        additional_answer = llm.invoke(prompt).content
        print("additional answer: " + additional_answer)
        return super().handle(input, lang, additional_answer=additional_answer)
