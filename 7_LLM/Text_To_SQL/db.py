import os
import pg8000 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection details
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT"))


def get_connection():
    conn = pg8000.connect(
        host=DB_HOST,  
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conn
