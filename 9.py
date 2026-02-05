import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

sentence = "The cats are running quickly"
tokens = word_tokenize(sentence)

# Define regex-based rules
patterns = [
    (r'.*ing$', 'VBG'),   # gerunds
    (r'.*ed$', 'VBD'),    # past tense verbs
    (r'.*s$', 'NNS'),     # plural nouns
    (r'^-?[0-9]+$', 'CD'),# numbers
    (r'.*', 'NN')         # default noun
]

tagger = RegexpTagger(patterns)
print(tagger.tag(tokens))
