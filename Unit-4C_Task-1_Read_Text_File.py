with open("data.txt", "w") as f:
    f.write("Hello, Welcome to Python\n")
    f.write("This is a text file\n")
    f.write("I am learning file handling")

print("--- File Content ---")
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

print("\n--- Line by Line ---")
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())