array2 = [2,4,6,8,10]
array1 = [5,2,5*3,3]
print(len(array1))
print(len(array2))
print(array1[1])
print(array2[3])
print(array2[len(array1)])
print(array1[len(array1)-1])
# That's not working because the second array has only 5 numbers and the print wants the 11th number.
#print(array2[10])