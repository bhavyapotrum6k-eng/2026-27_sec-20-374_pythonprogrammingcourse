number1 = float(input("Enter number1: "))
number2 = float(input("Enter number2: "))

print(f"({number1} > 5) and ({number2} < 50): {(number1 > 5) and (number2 < 50)}")
print(f"({number1} > 50) or ({number2} < 50): {(number1 > 50) or (number2 < 50)}")
print(f"not ({number1} > 50): {not (number1 > 50)}")