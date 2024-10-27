from sqlalchemy.orm import Session
from src.models.login import LoginRequest
from src.utils.database import crud, schemas
from src.utils.database.dependencies import get_db
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(
    prefix="/api",
    tags=["auth"]
)

security = HTTPBasic()

async def get_current_user(
    credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)
):
    """
    Get the current user from the database
    
    Args:
        credentials (HTTPBasicCredentials): The user credentials
        db (Session): The database session
        
    Returns:
        User: The user object
    """
    user = crud.get_user_by_username(db, credentials.username)
    if not user or not crud.verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user

@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user

    Args:
        user (UserCreate): The user details
        db (Session): The database session

    Returns:
        UserResponse: The user details
    """
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.post("/login")
def login(login_request: LoginRequest, db: Session = Depends(get_db), DBUser = Depends(get_current_user)):
    """
    Login a user

    Args:
        login_request (LoginRequest): The login details
        db (Session): The database session
        DBUser (User): The current user
    
    Returns:
        dict: The login message
    """
    db_user = crud.get_user_by_username(db, username=login_request.username_or_email)
    if not db_user:
        db_user = crud.get_user_by_email(db, email=login_request.username_or_email)
    if not db_user or not crud.verify_password(login_request.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return {"message": "Successfully logged in"}