import nltk
from nltk import word_tokenize, pos_tag

sentence = "The quick brown fox jumps over the lazy dog"
print(pos_tag(word_tokenize(sentence)))
