#Input 3 numbers and checking which one is the greatest
a = int(input("Enter no. 1 "))
b = int(input("Enter no. 2 "))
c = int(input("Enter no. 3 "))
if a > b and a > c:
    print("The greatest number is: ", a)
elif b > a and b > c:
    print("The greatest number is: ", b)
else: 
    print("The greatest number is: ", c)
