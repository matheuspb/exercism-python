import string

def is_pangram(text):
    return all(lc in text.lower() for lc in string.ascii_lowercase)
