import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def get_volumes(url):   # get links of all volumes from directory
    soup = bs(requests.get(url).text, 'html.parser')

    data = []
    for link in soup.find_all('a'):
        if link.text.startswith('humanist'):  # valid links have humanist label
            data.append(link.text)
    return data

def scrape_volume(url):  # scrape text
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    return soup.get_text()

def filter(doc):
    tmp =  ''.join([i for i in doc if i.isalpha() or i.isspace()]).replace('\n', ' ').replace('\r', '').lower() # filter to only alphabets and space
    while tmp.count('  ') > 0:
        tmp = tmp.replace('  ', ' ') 
    return tmp

if __name__ == '__main__':
    url = 'https://humanist.kdl.kcl.ac.uk/Archives/Converted_Text/' # base url
    scripts = []
    vols = get_volumes(url)
    for vol in vols:
        scripts.append({'url': url + vol, 'year': vol.split('.')[1], 'text': filter(scrape_volume(url + vol))})
    humanist_vols = pd.DataFrame(scripts)
    humanist_vols.to_csv('web_scraped_humanist_listserv.csv')

