import string

def is_isogram(word):
    clean = list(filter(lambda c: c.isalpha(), word.lower()))
    return len(clean) == len(set(clean))
