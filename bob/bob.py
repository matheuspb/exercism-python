import re

def hey(what):
    if re.search(r"^\s*$", what):
        return "Fine. Be that way!"
    elif what.isupper():
        return "Whoa, chill out!"
    elif re.search(r"\?\s*$", what):
        return "Sure."
    else:
        return "Whatever."
