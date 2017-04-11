# removes whitespaces from the end of the string
_trim = lambda string: _trim(string[0:-1]) if string[-1] == " " else string

def hey(what):
    if what.isspace() or not what:
        return "Fine. Be that way!"
    elif what.isupper():
        return "Whoa, chill out!"
    elif _trim(what)[-1] == "?":
        return "Sure."
    else:
        return "Whatever."
