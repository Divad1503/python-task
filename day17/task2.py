a = input("What do you want to encrypt ")
def coding(text):
    result = []
    for i in text:
        if 'a' <= i <= 'z':
            c = ord('a')
        elif 'A' <= i <= 'Z':
            c = ord('A')
        else:
            result.append(i)
            continue
        lett = chr((ord(i)- c + 13) % 26 + c)
        result.append(lett)
    return ''.join(result)
brief = coding(a)
print(brief)

        
