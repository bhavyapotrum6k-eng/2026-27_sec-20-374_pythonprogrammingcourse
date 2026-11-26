with open("simple.txt", "w") as f:
    f.write("Hi, This is my file")

with open("simple.txt", "r") as f:
    print(f.read())