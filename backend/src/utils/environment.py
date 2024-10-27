from dotenv import load_dotenv
import os
load_dotenv()

def set_environment(name, value):
    """
    Set the environment variable
    
    Args:
        name (str): The name of the environment variable
        value (str): The value of the environment variable
    """
    os.environ[name] = value

def get_environment(name):
    """
    Get the environment variable

    Args:
        name (str): The name of the environment variable

    Returns:
        str: The value of the environment variable
    """
    return os.getenv(name)

envs = [
"GROQ_API_KEY",
"HF_TOKEN",
]

def check_environment():
    """
    Check if the environment variables are set.
    """
    for env in envs:
        if not get_environment(env):
            raise Exception(f"Environment variable {env} not set")
        set_environment(env, get_environment(env))
        print(f"Environment variable {env} set")