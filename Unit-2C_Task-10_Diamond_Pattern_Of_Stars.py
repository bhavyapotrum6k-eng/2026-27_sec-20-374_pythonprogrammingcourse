n = int(input(f"Enter Number of rows: "))
# Top Half - Pyramid
for i in range(1, n + 1):
    for j in range(n - i):
        print(f" ", end=" ")
    for k in range(2 * i - 1):
        print(f"*", end=" ")
    print()

# Bottom Half - Inverted Pyramid
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(f" ", end=" ")
    for k in range(2 * i - 1):
        print(f"*", end=" ")
    print()