counter = 0  # Global variable

def increment():
    global counter
    counter = counter + 1
    print("Inside function, counter =", counter)

print("Before function call, counter =", counter)
increment()
increment()
increment()
print("After function calls, counter =", counter)