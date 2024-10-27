from . import models, schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    """
    Get the password hash
    
    Args:
        password (str): The password to hash
        
    Returns:
        str: The hashed password
    """
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """
    Verify the password

    Args:
        plain_password (str): The plain password
        hashed_password (str): The hashed password

    Returns:
        bool: True if the password is correct, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_username(db: Session, username: str):
    """
    Get the user by username

    Args:
        db (Session): The database session
        username (str): The username

    Returns:
        User: The user object
    """
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    """
    Get the user by email

    Args:
        db (Session): The database session
        email (str): The email

    Returns:
        User: The user object
    """
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    """
    Create a new user

    Args:
        db (Session): The database session
        user (UserCreate): The user details

    Returns:
        User: The user object
    """
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username_or_email: str, password: str):
    """
    Authenticate the user

    Args:
        db (Session): The database session
        username_or_email (str): The username or email
        password (str): The password

    Returns:
        User: The user object
    """
    user = get_user_by_username(db, username_or_email) or get_user_by_email(db, username_or_email)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user
