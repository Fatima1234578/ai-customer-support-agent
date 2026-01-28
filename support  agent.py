import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("tickets.csv")

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['ticket'])

def resolve_ticket(new_ticket):
    new_vec = vectorizer.transform([new_ticket])
    similarity = cosine_similarity(new_vec, X)
    best_match = similarity.argmax()

    return data.iloc[best_match]['category'], data.iloc[best_match]['response']
