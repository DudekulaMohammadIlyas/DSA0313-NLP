import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> DT NN | DT NNS
VP -> VBZ NP | VBP NP
DT -> 'the'
NN -> 'dog'
NNS -> 'cats'
VBZ -> 'chases'
VBP -> 'chase'
""")

parser = nltk.ChartParser(grammar)

def check_agreement(sentence):
    try:
        list(parser.parse(sentence))
        return "Sentence is grammatically correct."
    except ValueError:
        return "Sentence violates agreement rules."

print(check_agreement(['the','dog','chases','a','cats']))
print(check_agreement(['the','cats','chases','the','dog']))
