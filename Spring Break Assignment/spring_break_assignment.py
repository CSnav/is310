from bs4 import BeautifulSoup
import requests, os

# Imports raw_script_urls.txt (i dont know why but this is the only encoding that works for me)
raw = open('/Users/arnav/Git/is310-1/Spring Break Assignment/raw_script_urls.txt', encoding='ISO-8859-1')
lines = raw.readlines()
#print(len(lines))

# Get Movie Name
name=[]
for line in lines:
    name.append(line.split('+++$+++')[1].strip())

# Get URL
url=[]
for line in lines:
    url.append(line.split('+++$+++')[2].strip())

# Scrape the URL
def scrape(url):
    response = requests.get(url)
    return response.text

# Make files for each movie
for i in range(len(lines)):
    script = scrape(url[i])
    soup = BeautifulSoup(script, "html.parser")
    # Creates text files in a designated output folder because I got sick and tired of seeing so many text files clutter up my file explorer
    filename = str(i) + ' ' + name[i] + '.txt'
    finalpath = os.path.join("/Users/arnav/Git/is310-1/Spring Break Assignment/output", filename)
    with open(finalpath, "w") as f:
        f.write(str(soup))