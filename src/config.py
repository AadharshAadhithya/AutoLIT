from dotenv import load_dotenv
import os

from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()

class Config:
    def __init__(self):
        self.OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
        self.SCOPUS_API  = os.environ["SCOPUS_API"]
        self.DB_PATH = os.environ["DB_PATH"] #"sqlite:///database.db" 

        if not os.path.exists(os.environ["PDF_PATH"]):
            os.makedirs(self.PDF_PATH )
        
        self.PDF_PATH = os.environ["PDF_PATH"]




#Exports
settings = Config()
