P = float(input())
R = float(input())
T = float(input())
Total = P * (1 + R / 100) ** T
Compound = Total - P
print(Compound)