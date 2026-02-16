import spacy

nlp = spacy.load("en_core_web_sm")

text = "Rahul went to the bank. He deposited money."
doc = nlp(text)

sents = list(doc.sents)

if len(sents) >= 2:
    print("Similarity:", sents[0].similarity(sents[1]))
else:
    print("Need at least 2 sentences")
