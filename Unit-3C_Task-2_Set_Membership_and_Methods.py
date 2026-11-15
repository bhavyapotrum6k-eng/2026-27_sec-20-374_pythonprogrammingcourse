s = {1, 2, 3}
print("Set:", s)

# Membership testing
print("2 in s:", 2 in s)
print("5 in s:", 5 in s)
print("5 not in s:", 5 not in s)

# add()
s.add(4)
print("After add(4):", s)

# remove()
s.remove(2)
print("After remove(2):", s)
s.discard(3)
print("After discard(3):", s)
s.discard(10)
print("After discard(10) - no error:", s)