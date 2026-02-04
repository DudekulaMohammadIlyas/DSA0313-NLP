from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["running", "flies", "happily", "studies", "cats"]

stems = [stemmer.stem(word) for word in words]
print("Stems:", stems)
