from fastapi import FastAPI , Depends
from src.controllers.auth import get_current_user
from src.utils.environment import check_environment
from src.utils.database.database import engine, Base
from src.controllers.auth import router as auth_router
from src.controllers.agent_chat import router as chat_router
from src.controllers.upload_data import router as upload_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="RAG Chatbot API", description="API for chatbot using langchain, chroma and huggingface embeddings.", version="1.0")

@app.on_event("startup")
def startup_event():
    """
    Check the environment variables on startup
    """
    try:
        check_environment()
    except Exception as e:
        print(f"An unexpected error occurred during startup: {e}")

app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(chat_router)

@app.get("/api", tags=["root"], description="API working status check")
def root(DBUser = Depends(get_current_user)):
    """ 
    API working status check
    """
    return {"API is working": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)