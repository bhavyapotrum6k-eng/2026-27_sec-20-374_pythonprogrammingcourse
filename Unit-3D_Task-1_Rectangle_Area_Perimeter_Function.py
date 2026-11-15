def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

a, p = rectangle(10, 5)
print("Length: 10, Breadth: 5")
print("Area:", a)
print("Perimeter:", p)