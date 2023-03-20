import requests
from bs4 import BeautifulSoup


def download_and_save_pdf(doi,save_dir):


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
 
    # Download the paper using the download link
    with open(save_dir, 'wb') as f:
        f.write(requests.get(download_link).content)