from sqlalchemy import Column,String,Integer,create_engine


from database import Base
import re
        


class Paper(Base):
    __tablename__ = 'paper'
    pub_url = Column(String)
    title = Column(String,primary_key=True)
    pub_year = Column(String)
    publisher_name= Column(String)
    abstract = Column(String)
    num_citations = Column(Integer)
    eprint_url = Column(String)
    pdf_path = Column(String)
    scrape_source = Column(String)
    
    def __init__(self, pub_dict):
        self.pub_url = pub_dict['pub_url']
        self.title =  re.sub(' ','-', re.sub(r'[^A-Za-z0-9 ]+', '',   pub_dict['bib']['title'].lower()))
        self.pub_year = pub_dict['bib']['pub_year']
        self.publisher_name = pub_dict['bib']['venue'].lower()
        #self.abstract = pub_dict['bib']['abstract']
        self.num_citations = pub_dict['num_citations']
        self.eprint_url = pub_dict['eprint_url']


