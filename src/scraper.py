
from scholarly import scholarly

class Scraper:

    def __init__(self,gsq,sq=None) :
        """
        Scrapes google and scopus for given queries and returns relevent informations

        Params
        =======
        gsq: Google Scholar Query, expected as a list/
        sq: Scopus Query, expected as a string of scopus boolean query
        
        """
        self.gsq = gsq

    def scrape_google_scholar(self):
        self.gs_results = scholarly.search_pubs(self.gsq)
    

    def scrape_scopus(self):
        pass
