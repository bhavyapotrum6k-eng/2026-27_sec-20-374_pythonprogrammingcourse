def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

print("With default rate (5):", simple_interest(10000, 2))
print("With explicit rate (8):", simple_interest(10000, 2, 8))