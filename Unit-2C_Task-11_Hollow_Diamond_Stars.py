n = int(input(f"Enter n: "))
# Top Half
for i in range(1, n + 1):
    print(f"{' ' * (n - i)}", end="")
    if i == 1:
        print(f"*")
    else:
        print(f"* {' ' * (2 * i - 3)}*")

# Bottom Half
for i in range(n - 1, 0, -1):
    print(f"{' ' * (n - i)}", end="")
    if i == 1:
        print(f"*")
    else:
        print(f"* {' ' * (2 * i - 3)}*")