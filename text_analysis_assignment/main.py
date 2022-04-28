import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english')) # set of stop words: the, as, etc

def top_1_year(df, year, verbose=False):  
    doc = df[df['year'] == year].text.item()   # get text from df
    words = nltk.tokenize.word_tokenize(doc)   # extract words
    dists = nltk.FreqDist(w for w in words if w not in stop_words)
    
    if verbose:
        return dists

    return dists.most_common(1)[0]

def top_1_all(df):
    doc = ' '.join(df.text.to_list())
    words = nltk.tokenize.word_tokenize(doc)
    dists = nltk.FreqDist(w for w in words if w not in stop_words)

    return dists.most_common(1)[0]

def plot(df, word):
    x, y = [], []   # add year to x, freq to y
    for i, row in df.iterrows():
        dist = top_1_year(df, row.year, verbose=True)
        if word not in dist:
            raise ValueError('word not found')  # raise error if word not in text
        x.append(row.year)
        y.append(dist[word])
    plt.plot(x, y)
    plt.show()

df = pd.read_csv('../notebook_assignment/web_scraped_humanist_listserv.csv')
print(top_1_year(df, '1987-1988'))
plot(df, 'I')