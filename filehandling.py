# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a file handling example in Python.\n")
    file.write("Writing to a file is easy.\n")


# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()

print("File Content:")
print(content)

# Appending to a file
with open('example.txt', 'a') as file:
    file.write("Appending a new line to the file.\n")

# Reading from the file again to see appended content
with open('example.txt', 'r') as file:
    content = file.read()

print("Updated File Content:")
print(content)
