def split(string):
    words = ['']
    i = 0
    for char in string:
        if char.isalpha() or char.isnumeric():
            words[i] += char.lower()
        else:
            words.append('')
            i += 1
    return [word for word in words if word != '']


def word_count(phrase):
    d = {}
    for word in split(phrase):
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d
