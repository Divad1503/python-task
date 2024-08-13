def min(liste):
    a = liste[0]
    for i in liste:
        if i < a:
            a = i
    return a
def max(liste):
    a = liste[0]
    for i in liste:
        if i > a:
            a = i
    return a

def mid(liste):
    sum = 0
    for i in range(len(liste)):
        sum = sum + liste[0+i]
    amount = len(liste)
    mid = sum / amount
    return mid
numbers = [8,5,12,3,7]
min_number = min(numbers)
max_number = max(numbers)
mid_number = mid(numbers)
print(min_number,max_number,mid_number)