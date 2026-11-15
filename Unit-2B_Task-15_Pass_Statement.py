print("1) Pass using for loop:")
for i in range(1, 11):
    if i == 6:
        pass
    print(i, end=" ")
print("\npass did nothing, 6 is also Printed")

print("\n2) Pass using while loop:")
i = 1
while i <= 10:
    if i == 6:
        pass
    print(i, end=" ")
    i = i + 1
print("\nPass did nothing, 6 is also Printed")