t1 = (10, 20, 30)
t2 = (40, 50)
t3 = t1 + t2
print("concatenation:", t3)
print("slicing [1:4]:", t3[1:4])
print("slicing [:3]:", t3[:3])
print("slicing [::-1]:", t3[::-1])
a, b, c, d, e = t3
print("unpacking:", a, b, c, d, e)