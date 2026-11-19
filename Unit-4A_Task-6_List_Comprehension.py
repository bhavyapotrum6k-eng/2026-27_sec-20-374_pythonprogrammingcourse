numbers = [1, 2, 3, 4, 5, 6]
squares = [x * x for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
print('Squares:', squares)
print('Even Numbers:', evens)