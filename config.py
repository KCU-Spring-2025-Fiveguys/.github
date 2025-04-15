import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로드

API_KEY = os.getenv("OPENAI_API_KEY")
