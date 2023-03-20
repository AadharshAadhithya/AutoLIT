from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()

class Config:
    def __init__(self):
        self.OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
        self.SCOPUS_API  = os.environ["SCOPUS_API"]



# Database Configurations

engine = create_engine('sqlite:///database.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#Exports
config = Config()