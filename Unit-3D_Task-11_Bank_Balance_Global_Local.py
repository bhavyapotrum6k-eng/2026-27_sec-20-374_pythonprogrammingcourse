balance = 1000  # Global balance

def deposit(amount):
    global balance
    balance = balance + amount
    print("Deposited:", amount, "Rs")
    print("Balance after deposit (global):", balance, "Rs")

def fake_deposit(amount):
    balance = 0  # Local balance - does NOT update global
    balance = balance + amount
    print("Inside fake_deposit, local balance =", balance, "Rs")

print("Initial balance:", balance, "Rs")
deposit(500)
fake_deposit(500)
print("Final balance (account):", balance, "Rs")