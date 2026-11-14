n = int(input("Enter how many Numbers: "))
largest = float("-inf")

for i in range(n):
    num = float(input("Enter a number: "))
    if num > largest:
        largest = num

print("Largest Number is : ", largest)