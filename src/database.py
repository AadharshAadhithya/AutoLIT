from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings



# Database Configurations

engine = create_engine(settings.DB_PATH)
Session = sessionmaker(bind=engine)

#exports
Base = declarative_base()
session = Session()