n = int(input(f"Enter n: "))
for i in range(n):
    print(f"{' ' * (n - i - 1)}", end="")
    val = 1
    for j in range(i + 1):
        print(f"{val} ", end="")
        val = val * (i - j) // (j + 1)
    print()