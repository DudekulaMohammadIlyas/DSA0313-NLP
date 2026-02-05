training = [("dog","NN"),("barks","VBZ"),("cat","NN"),("meows","VBZ"),("the","DT")]
prob = {}
for w,t in training: prob[w] = t

def tag(sentence):
    return [(w, prob.get(w,"NN")) for w in sentence.split()]

print(tag("the dog barks at the cat"))
