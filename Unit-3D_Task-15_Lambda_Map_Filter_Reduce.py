from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda x: x * x, numbers))
print("Original:", numbers)
print("Squares using map() + lambda:", squares)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter() + lambda:", evens)

total = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce() + lambda:", total)