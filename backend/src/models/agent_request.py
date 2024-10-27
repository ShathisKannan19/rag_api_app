from pydantic import BaseModel
from typing import List, Dict, Any

class AgentRequest(BaseModel):
    query: str
    chat_history: List[Dict[str, Any]]