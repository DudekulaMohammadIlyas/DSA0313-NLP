text = "Rahul went home. He was tired."

name = text.split()[0]
resolved = text.replace("He", name)

print("Resolved Text:", resolved)
