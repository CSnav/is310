import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def get_volumes(url):
    soup = bs(requests.get(url).text, 'html.parser')

    data = []
    for link in soup.find_all('a'):
        if link.text.startswith('humanist'):
            data.append(link.text)
    return data

def scrape_volume(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    return soup.get_text()

if __name__ == '__main__':
    url = 'https://humanist.kdl.kcl.ac.uk/Archives/Converted_Text/'
    scripts = []
    vols = get_volumes(url)
    for vol in vols:
        scripts.append({'url': url + vol, 'year': vol.split('.')[1], 'text': scrape_volume(url + vol)})
    humanist_vols = pd.DataFrame(scripts)
    humanist_vols.to_csv('web_scraped_humanist_listserv.csv')

