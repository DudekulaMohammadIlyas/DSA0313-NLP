import nltk
from nltk import word_tokenize, pos_tag

sentence = "The cats a running"
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)

# Simple transformation rule: if 'cats' is plural, change verb 'is' → 'are'
transformed = []
for word, tag in tags:
    if word == "is" and ("cats", "NNS") in tags:
        transformed.append((word, "VBP"))  # plural verb
    else:
        transformed.append((word, tag))

print("Before:", tags)
print("After:", transformed)
