import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> DT NN | DT NNS
VP -> VB NP | VBZ NP | VBG NP
DT -> 'the'
NN -> 'dog'
NNS -> 'cats'
VB -> 'chased'
VBZ -> 'is'
VBG -> 'running'
""")

parser = nltk.ChartParser(grammar)
sentence = ['the', 'dog', 'chased', 'the', 'cats']
for tree in parser.parse(sentence):
    print(tree)
