with open("sample.txt", "w") as f:
    f.write("Hello Python\nFile Handling is easy")

with open("sample.txt", "r") as f:
    data = f.read()

print("Lines:", len(data.splitlines()))
print("Words:", len(data.split()))
print("Characters:", len(data))