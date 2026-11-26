with open("source.txt", "w") as f:
    f.write("Hello, Copy this file")

with open("source.txt", "r") as f1, open("destination.txt", "w") as f2:
    f2.write(f1.read())

print("Copied Successfully!")