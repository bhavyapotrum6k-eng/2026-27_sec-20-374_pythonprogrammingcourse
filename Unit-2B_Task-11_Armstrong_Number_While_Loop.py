num = int(input("Enter a 3-digit number: "))
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total = total + digit ** 3
    temp = temp // 10

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")