import requests
from bs4 import BeautifulSoup
import os
from config import settings
from database import session

def clear_db(Table):
    session.query(Table).delete()
    session.commit()


def clear_pdfs():
    for f in os.listdir(settings.PDF_PATH):
        os.remove(os.path.join(settings.PDF_PATH, f))


def download_and_save_pdf(doi,save_dir):

    if doi.split(".")[-1] == "pdf":
     
        download_link = doi
       
    else:
        base_url = 'https://sci-hub.se/'
        response = requests.get(base_url + doi.strip())
        soup = BeautifulSoup (response.content, 'html.parser')
        content = soup.find('embed').get('src').replace('#navpanes=0&view=FitH', '').replace('//', '/') 
        if content.startswith('/downloads'):
            pdf = 'https://sci-hub.se' + content
        elif content.startswith('/tree'):
            pdf = 'https://sci-hub.se' + content
        elif content.startswith('/uptodate'): 
            pdf = 'https://sci-hub.se' + content 
        else:
            pdf = 'https:/sci-hub.se'+ content

   

        # Make a request to Sci-Hub to get the download link for the paper
        response = requests.get(pdf)

        # Extract the download link from the response
        download_link = response.url

    print(download_link)
    print(save_dir)

    # Download the paper using the download link
    with open(save_dir, 'wb') as f:
        f.write(requests.get(download_link).content)