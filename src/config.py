from dotenv import load_dotenv
import os


load_dotenv()

class Config:
    def __init__(self):
        self.OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
        self.SCOPUS_API  = os.environ["SCOPUS_API"]




config = Config()