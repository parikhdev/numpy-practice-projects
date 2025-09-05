#WAP to check if a list contains Palindrome of elemets
list = [2,3,3,1]
print(list)
if (list == list[::-1]):
    print("The list is a Palindrome")
else:
    print("The list is not a Palindrome")

    
# Methods of List:
                # Append
list.append(4)
print(list)
                # Reverse
list.reverse()
print(list)
                # Insert(indx, element)
list.insert(3, 7)
print(list)
                # Sort
list.sort()
print(list)
                # Sort in reverse
list.sort(reverse=True)
print(list)
                # Remove
list.remove(7)
print(list)
                #Pop(indx)
list.pop(0)
print(list)