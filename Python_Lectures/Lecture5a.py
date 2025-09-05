# Search for a number X in the tupple using a while loop
# 1, 4, 9, 16, 25, 36, 49, 64, 81, 100

# let suppose x is 64

tupple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 64)

x = 61
''' While Loop '''
i = 0
while i < len(tupple):
    if tupple[i] == x:
        print("The element is found at index: ", i)
    i += 1
else: 
    print("End")


''' For Loop '''
# i = 0
# for val in tupple:
#     if val == x:
#         print("The element is found at index:", i)
#     i += 1
