from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional, Dict, Any

class State(TypedDict):
    user_input: str
    intent: Optional[str]
    entities: Optional[Dict[str, Any]]
    tool_result: Optional[Any]
    final_answer: Optional[str]