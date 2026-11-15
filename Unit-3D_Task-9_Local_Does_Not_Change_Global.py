x = 10  # Global variable

def show():
    x = 50  # Local variable with same name
    print("Inside function, x =", x)

show()
print("Outside function, x =", x)