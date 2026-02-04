import re

text = "The rain in Spain falls mainly in the plain."

# Match words starting with 'S'
pattern = r"\bS\w+"
matches = re.findall(pattern, text)
print("Words starting with 'S':", matches)

# Search for 'rain'
search_result = re.search(r"rain", text)
if search_result:
    print("Found 'rain' at position:", search_result.start())
