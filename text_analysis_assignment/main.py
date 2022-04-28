import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
import pandas as pd

def top_1_year(df, year):
    doc = str(df[df['year'] == year].text)
    words = nltk.tokenize.word_tokenize(doc)
    dists = nltk.FreqDist(w.lower() for w in words)

    return dists.most_common(1)

def top_1_all(df):
    doc = '\n'.join(df.text.to_list())
    words = nltk.tokenize.word_tokenize(doc)
    dists = nltk.FreqDist(w.lower() for w in words)

    return dists.most_common(1)



if __name__ == '__main__':
    df = pd.read_csv('../notebook_assignment/web_scraped_humanist_listserv.csv')
    print(top_1_all(df))