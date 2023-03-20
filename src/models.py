from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings



# Database Configurations

engine = create_engine(settings.DB_PATH)

Session = sessionmaker(bind=engine)
Base = declarative_base()

session = Session()




        


class Paper(Base):
    __tablename__ = 'paper'
    pub_url = Column(String, primary_key=True)
    title = Column(String)
    pub_year = Column(String)
    venue = Column(String)
    abstract = Column(String)
    num_citations = Column(Integer)
    eprint_url = Column(String)
    
    def __init__(self, pub_dict):
        self.pub_url = pub_dict['pub_url']
        self.title = pub_dict['bib']['title']
        self.pub_year = pub_dict['bib']['pub_year']
        self.venue = pub_dict['bib']['venue']
        self.abstract = pub_dict['bib']['abstract']
        self.num_citations = pub_dict['num_citations']
        self.eprint_url = pub_dict['eprint_url']


