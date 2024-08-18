print("Which numbers are in the array? Write the numbers one after one and write 'stop' to see all sets\n ")
arr = []
# while True:
#     a = input("")
#     if a == "stop":
#         break
#     else:
#         b = int(a)
#         arr.append(b)
my_set = {1,2} # {}, {1}, {2}, {1,2}
#1,2,3 {}, {1}, {2}, {3}, {1, 2},  {1, 3}, {2, 3}, {1,2,3}
for i in my_set:
    print(i)
    # for h in range(len(my_set)-i):
    #     print(my_set)

