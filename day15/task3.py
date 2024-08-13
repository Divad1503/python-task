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

def mean(liste):
    sum = 0
    for i in range(len(liste)):
        sum = sum + liste[0+i]
    amount = len(liste)
    mean_num = sum / amount
    return mean_num


numbers = [8,5,12,3,7]
min_number = min(numbers)
max_number = max(numbers)
mean_number = mean(numbers)
print(min_number,max_number,mean_number)