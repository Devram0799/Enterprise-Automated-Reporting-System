import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text
from config.config import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT DB_NAME()"))
        print("Connected Successfully!")
        print("Database:", result.scalar())
except Exception as e:
    print("Connection Failed")
    print(e)