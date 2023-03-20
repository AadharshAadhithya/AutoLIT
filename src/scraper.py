
from scholarly import scholarly
from tqdm import tqdm
from database import session
from models import Paper
from config import settings
from utils import download_and_save_pdf
import os


class Scraper:

    def __init__(self,gsq,gsq_limit=5,sq=None) :
        """
        Scrapes google and scopus for given queries and returns relevent informations

        Params
        =======
        gsq: Google Scholar Query, expected as a list/
        sq: Scopus Query, expected as a string of scopus boolean query
        gsq_limit: maximum number of papers to limit from google scholar search results
        
        """
        self.gsq = gsq
        self.gsq_limit = gsq_limit


    def scrape_google_scholar(self):

        self.gs_results = scholarly.search_pubs(self.gsq)
        for i in tqdm(range(self.gsq_limit)):
            p = next(self.gs_results)
            res = session.query(Paper).filter(Paper.title == p["bib"]["title"]).first()
            if res is None:
                paper = Paper(p)
                save_path = os.path.join(settings.PDF_PATH, paper.title+".pdf")  
                download_and_save_pdf(paper.eprint_url,save_dir=save_path)
                paper.pdf_path = save_path
                session.add(paper)
                session.commit()
        

    
    

    def scrape_scopus(self):
        pass
