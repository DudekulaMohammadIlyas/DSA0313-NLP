import spacy

nlp = spacy.load("en_core_web_sm")
sentence = "The smart student solved the problem."

doc = nlp(sentence)
for chunk in doc.noun_chunks:
    print(chunk.text)
