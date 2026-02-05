import random

text = "the cat sat on the mat the cat ate food"
words = text.split()

# Build bigram model
model = {}
for i in range(len(words)-1):
    model.setdefault(words[i], []).append(words[i+1])

# Generate text
word = "the"
output = [word]
for _ in range(9):
    word = random.choice(model.get(word, [""]))
    output.append(word)
print("Generated:", " ".join(output))
