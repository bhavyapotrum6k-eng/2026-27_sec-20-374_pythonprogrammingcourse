num = int(input("Enter a number: "))
reverse = 0
temp = num

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if reverse == num:
    print(num, "is a Palindrome number")
else:
    print(num, "is NOT a Palindrome number")