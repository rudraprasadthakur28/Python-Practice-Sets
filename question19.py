with open("test.txt", "w") as file:
    file.write("Hello")

with open("test.txt", "a") as file:
    file.write(" World")

with open("test.txt") as file:
    content = file.read()

print(content)