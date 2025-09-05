# with open("sample.txt", "r") as file:
#     content = file.read()
#     word = "Java"
#     if word in content:
#         print("Found!")
#     else:
#         print("Not Found!")

def find_word(word):
 data = True
 Line_no = 1
 with open("sample.txt", "r") as file:
     while data:
         data = file.readline()
         if word in data:
             print(Line_no)
             return
         Line_no += 1
     return -1

print(find_word("learning"))






