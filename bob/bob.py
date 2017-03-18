def _trim(string):
    if string[-1] == " ":
        return _trim(string[0:-1])
    else:
        return string

def hey(what):
    clean = list(filter(lambda c: c.isalpha(), what))

    if all(c.isspace() for c in what):
        return "Fine. Be that way!"
    elif (all(c.isupper() for c in clean) and clean):
        return "Whoa, chill out!"
    elif _trim(what)[-1] == "?":
        return "Sure."
    else:
        return "Whatever."
