def fsa_match_ab(string):
    state = 0
    for char in string:
        if state == 0:
            state = 1 if char == 'a' else 0
        elif state == 1:
            state = 2 if char == 'b' else (1 if char == 'a' else 0)
        elif state == 2:
            state = 2 if char == 'b' else (1 if char == 'a' else 0)
    return state == 2 and string.endswith("ab")

# Test
print(fsa_match_ab("cab"))   # True
print(fsa_match_ab("abc"))   # False
print(fsa_match_ab("ab"))    # True
