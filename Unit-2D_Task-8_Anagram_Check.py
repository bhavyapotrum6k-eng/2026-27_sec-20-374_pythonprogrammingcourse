s1 = input(f"Enter first string: ").lower()
s2 = input(f"Enter second string: ").lower()
if sorted(s1) == sorted(s2):
    print(f"Anagrams")
else:
    print(f"Not Anagrams")