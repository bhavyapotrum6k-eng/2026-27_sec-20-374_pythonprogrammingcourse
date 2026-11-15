rows = int(input(f"Enter Number of rows: "))
symbol = input(f"Enter a symbol: ")
for i in range(1, rows + 1):
    for j in range(i):
        print(f"{symbol}", end=" ")
    print()