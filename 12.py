import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> DT NN | DT NNS
VP -> VB NP
DT -> 'the'
NN -> 'dog'
NNS -> 'cats'
VB -> 'chased'
""")

parser = nltk.EarleyChartParser(grammar)
sentence = ['the', 'dog', 'chased', 'the', 'cats']
for tree in parser.parse(sentence):
    print(tree)
