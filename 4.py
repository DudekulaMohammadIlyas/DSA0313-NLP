def pluralize(noun):
    if noun.endswith('y') and noun[-2] not in 'aeiou':
        return noun[:-1] + 'ies'
    elif noun.endswith(('s', 'sh', 'ch', 'x', 'z')):
        return noun + 'es'
    else:
        return noun + 's'

# Test
nouns = ["cat", "dog", "baby", "box", "church"]
plurals = [pluralize(n) for n in nouns]
print("Plural Forms:", plurals)
