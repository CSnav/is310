import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def scrape():
    url = 'https://humanist.kdl.kcl.ac.uk/Archives/Converted_Text/'
    soup = bs(requests.get(url).content, 'html.parser')

    data = []
    for link in soup.find_all('a'):
        if link.text.startswith('humanist'):
            data.append({'Year': link.text.split('.')[1], 'Text': requests.get(url + link.text).text})
    return data

if __name__ == '__main__':
    data = scrape()
    humanist_vols = pd.DataFrame.from_records(data)
    print(humanist_vols.head())
    humanist_vols.to_csv('web_scraped_humanist_listserv.csv')

