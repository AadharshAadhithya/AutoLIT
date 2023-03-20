from database import session
from scraper import Scraper
from models import Paper
from config import settings
import os
from utils import download_and_save_pdf,clear_pdfs,clear_db
from tqdm import tqdm
import re





if __name__ == "__main__":

    clear_db(Paper)
    clear_pdfs()

    gs_query = "Covid-19 Forecasting"
    scraper = Scraper(gsq=gs_query)
    scraper.scrape_google_scholar()

    # count = 2

    # for i in tqdm(range(count)):
    #     p = next(results)
    #     res = session.query(Paper).filter(Paper.title == p["bib"]["title"]).first()
    #     if res is None:
    #         paper = Paper(p)
    #         save_path = os.path.join(settings.PDF_PATH, paper.title+".pdf")  
    #         download_and_save_pdf(paper.eprint_url,save_dir=save_path)
    #         paper.pdf_path = save_path
    #         session.add(paper)
    #         session.commit()
