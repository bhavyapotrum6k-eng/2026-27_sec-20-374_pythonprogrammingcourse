num = int(input("Enter a number: "))
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total = total + digit
    temp = temp // 10

print("Sum of digits of", num, "is:", total)