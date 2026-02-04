import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "Dogs are running in the park"
tokens = word_tokenize(sentence)
morph_analysis = pos_tag(tokens)

print("Morphological Analysis:", morph_analysis)
