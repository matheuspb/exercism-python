def encode(string):
    string += "\n"
    encoded = ""
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            if count > 1:
                encoded += (str(count) + string[i-1])
            else:
                encoded += string[i-1]
            count = 1

    return encoded


def decode(string):
    last = 0
    l = []
    for i in range(len(string)):
        if not (string[i].isdigit() and string[i+1].isdigit()):
            l += [string[last:i+1]]
            last = i + 1

    decoded = ""
    i = 0
    while i < len(l):
        if l[i].isdigit():
            decoded += int(l[i])*l[i+1]
            i += 2
        else:
            decoded += l[i]
            i += 1

    return decoded
