import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL: str = os.getenv("BASE_URL","https://restful-booker.herokuapp.com")
    USERNAME: str = os.getenv("DEFAULT_USERNAME","admin")
    PASSWORD: str = os.getenv("DEFAULT_PASSWORD","password123")

settings = Settings()


