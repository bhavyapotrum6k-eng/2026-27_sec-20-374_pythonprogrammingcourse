with open("data.txt", "w") as f:
    f.write("Python is easy")

with open("data.txt", "r") as f:
    data = f.read().replace("Python", "Java")

with open("data.txt", "w") as f:
    f.write(data)

print(data)