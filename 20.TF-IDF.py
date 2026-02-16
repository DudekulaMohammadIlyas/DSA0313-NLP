from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
    "I love machine learning",
    "Machine learning is powerful",
    "Python is great for AI"
]

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(docs)

query = vectorizer.transform(["machine learning"])
scores = cosine_similarity(query, tfidf)

print(scores)
