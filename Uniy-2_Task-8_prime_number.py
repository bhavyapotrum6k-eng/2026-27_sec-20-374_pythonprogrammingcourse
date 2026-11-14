num = int(input("Enter a number b/w 1 and 100: "))

if num == 1:
    print(num, "is not a Prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a Prime number")
    else:
        print(num, "is not a Prime number")