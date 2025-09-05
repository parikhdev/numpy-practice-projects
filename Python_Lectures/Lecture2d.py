#  Check the largest among the 10 numbers, entered by the user
# largest = None
# for i in range(10):
#     num = int(input("Enter number {}: ".format(i + 1)))
#     if largest is None or num > largest:
#         largest = num
# print("The largest number is:", largest)

nums = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
print(f"The Largest No. is: {max(nums)}")
