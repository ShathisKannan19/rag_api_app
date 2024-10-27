from fastapi import APIRouter , Depends
from src.controllers.auth import get_current_user
from src.models.agent_request import AgentRequest
from src.services.chat_service import chat_service

router = APIRouter( prefix="/api", tags=["rag_part"])

@router.post("/agent_chat", description="Chat with the AI as RAG Chatbot")
def agent_chat(request: AgentRequest, DBUser = Depends(get_current_user)):
    """ Chat with the AI as RAG Chatbot

    Args:
        request (AgentRequest): Request body for the chat with the AI as RAG Chatbot
        DBUser (, optional): User Details. Defaults to Depends(get_current_user).

    Returns:
        str: Response from the AI as RAG Chatbot
    """
    respose = chat_service(request.query, request.chat_history, DBUser.username)
    return respose