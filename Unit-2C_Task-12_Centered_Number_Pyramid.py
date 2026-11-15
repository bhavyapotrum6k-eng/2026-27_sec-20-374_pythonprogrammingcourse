n = int(input(f"Enter n: "))
for i in range(1, n + 1):
    print(f"{' ' * (n - i)}", end="")
    for j in range(1, i + 1):
        print(f"{j} ", end="")
    for j in range(i - 1, 0, -1):
        print(f"{j} ", end="")
    print()