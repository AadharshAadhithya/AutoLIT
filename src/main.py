from models import session

from scraper import Scraper

from models import Paper


if __name__ == "__main__":

    gs_query = "Covid-19 Forecasting"
    scraper = Scraper(gsq=gs_query)
    scraper.scrape_google_scholar()
    res = next(scraper.gs_results)

    paper = Paper(res)

    session.add(paper)

    session.commit()

    papers = Paper.query.all()

    for paper in papers:
        print(paper.title)
