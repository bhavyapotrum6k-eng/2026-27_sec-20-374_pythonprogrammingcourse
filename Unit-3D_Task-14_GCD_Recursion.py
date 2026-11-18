def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print("GCD of 48 and 18:", gcd(48, 18))
print("GCD of 12 and 15:", gcd(12, 15))
print("GCD of 7 and 13:", gcd(7, 13))