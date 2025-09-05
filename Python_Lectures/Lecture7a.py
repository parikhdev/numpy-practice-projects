# with open ("sample.txt", "r+") as f:
#     content = f.read()
    
# New_content = content.replace("Java", "Python")

# with open("sample.txt", "w+") as f:
#     f.write(New_content)
#     print(New_content)

# Step 1: Read lines
with open("sample.txt", "r") as file:
    lines = file.readlines()

# Step 2: Insert a new line at position 2 (indexing starts at 0)
lines.insert(2, "Python is very powerful!\n")

# Step 3: Write back
with open("sample.txt", "w") as file:
    file.writelines(lines)
