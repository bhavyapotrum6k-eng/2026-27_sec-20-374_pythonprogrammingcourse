n = int(input(f"Enter Number of rows: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(f"*", end=" ")
    print()