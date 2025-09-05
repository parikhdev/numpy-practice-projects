# WAP to enter the marks of 3 subjects from the user. 
# Fill them in an empty dictionary and add one by one
# such that the subjects are the keys and the marks are the values

Result = {}

Maths_Marks = int(input("Enter the marks of Maths: ")) 
English_Marks = int(input("Enter the marks of English: ")) 
Science_Marks = int(input("Enter the marks of Science: ")) 

# Result.update({"Maths": Maths_Marks})
# Result.update({"English": English_Marks})
# Result.update({"Science": Science_Marks})
# print(Result)

Result["Maths"] = Maths_Marks
Result["English"] = English_Marks
Result["Science"] = Science_Marks
print(Result)