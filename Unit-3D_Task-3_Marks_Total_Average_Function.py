def total_average(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

t, a = total_average(80, 90, 70)
print("Marks: 80, 90, 70")
print("Total:", t)
print("Average:", a)