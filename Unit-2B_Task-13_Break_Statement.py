print("1) break using for loop:")
for i in range(1, 11):
    if i == 6:
        break
    print(i, end=" ")
print("\nLoop stopped at 6")

print("\n2) break using while loop:")
i = 1
while i <= 10:
    if i == 6:
        break
    print(i, end=" ")
    i = i + 1
print("\nLoop stopped at 6")