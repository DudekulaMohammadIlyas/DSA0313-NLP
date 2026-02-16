import re

expr = "Likes(John, Mary)"
match = re.match(r"(\w+)\((\w+),(\w+)\)", expr)

if match:
    print("Predicate:", match.group(1))
    print("Arguments:", match.group(2), match.group(3))
