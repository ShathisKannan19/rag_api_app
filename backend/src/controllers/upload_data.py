import os
import shutil
from fastapi.responses import JSONResponse
from src.controllers.auth import get_current_user
from fastapi import APIRouter, UploadFile, Depends
from src.services.upload_service import load_the_docs

router = APIRouter( prefix="/api", tags=["rag_part"])

@router.post("/uploadfile", tags=["rag_part"], description="Now, We only accept .pdf files for now.")
async def upload_file(file: UploadFile, DBUser = Depends(get_current_user)):
    """
    Upload a file to the server

    Args:
        file (UploadFile): The file to upload
        DBUser (, optional): User Details. Defaults to Depends(get_current_user).

    Returns:
        JSONResponse: The file details
    """
    # Create the directory if it doesn't exist
    os.makedirs(f"src/data/{DBUser.username}", exist_ok=True)
    
    # Generate a unique filename (you might want to improve this)
    file_location = f"src/data/{DBUser.username}/{file.filename}"
    
    # Save the file
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    # populate_database()
    load_the_docs(DBUser.username)
    
    return JSONResponse(content={
        "filename": file.filename,
        "file_size": os.path.getsize(file_location),
        "file_path": file_location
    })