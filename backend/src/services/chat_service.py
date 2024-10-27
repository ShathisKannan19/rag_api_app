# Compile the graph
from langchain_groq import ChatGroq
from src.utils.shared import embeddings
from langchain_chroma import Chroma
from src import GROQ_API_KEY as GROQ_API
from langchain_core.prompts.prompt import PromptTemplate

def retrieve_data(query, USER):
  embedding_function = embeddings
  CHROMA_PATH = f"src/chroma/{USER}"
  db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
  results = db.similarity_search(query, k=2)
  print(results)
  return results

def chat_service(request, chat_history, USER):
    """
    Chat service for the chatbot.

    Args:
        request(dict): The request body

    Returns:
        str: The response
    """
    context = retrieve_data(request, USER)
    user_prompt = f"""
    You are an expert conversation bot.
     - You need to converse using the Questio/Answer/Chat Hostory below provided.
     - Only you response as a bot.

    Question: {request}

    Answer: {context}

    Chat History: {chat_history}

    **Instructions:**
    - If the user gave the greeting, respond with a greeting.
    - If the user asked a question, provide an answer.
    - If the user asked for help, provide assistance.

    **Example:**
    - User: Hi, how are you?
    - Bot: Hi! I'm doing well. How can I help you today?
    
    - User: What is the capital of France?
    - Bot: The capital of France is Paris.

    """
    llm = ChatGroq(
        model="mixtral-8x7b-32768",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # other params...
        api_key= GROQ_API
    )
    prompt =[
    (
        "system",
        "You are an expert to explain the following question bsed on the answer we have provided.",
    ),
    ("human", user_prompt),
    ]


    response = llm.invoke(prompt)
    response = response.content
    return response