int_list = [979, 366,1721,299,675,1456]
#def number():


for h in range(len(int_list)):
    for i in range(1,len(int_list)):
        c = 0
        d = 0
        a = int_list[0 + h]
        b = int_list[0 + i]
        if b + a == 2020:
            e = b * a
            print(e)
            break
        