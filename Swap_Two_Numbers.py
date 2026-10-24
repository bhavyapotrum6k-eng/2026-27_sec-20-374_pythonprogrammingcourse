a = int(input("enter a number:"))
b = int(input("enter a number:"))

a, b = b, a
print("after swap approach 1:")
print(a)
print(b)

a, b = b, a

a = a + b
b = a - b
a = a - b
print("after swap approach 2:")
print(a)
print(b)