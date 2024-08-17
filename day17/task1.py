a = input("What text do you need to decrypt? ")
def coding(text):
    result = []
    for h in text:
        if 'a' <= h <= 'z':
            c = ord('a')
        elif 'A' <= h <= 'Z':
            c = ord('A')
        else:
            result.append(h)
            continue
        letter = chr((ord(h) - c + 13) % 26 + c)
        result.append(letter)
    return ''.join(result)
end = coding(a)
print(end)
