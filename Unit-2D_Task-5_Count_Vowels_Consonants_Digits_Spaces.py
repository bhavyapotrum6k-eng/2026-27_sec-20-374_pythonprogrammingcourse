s = input(f"Enter a string: ")
v = c = d = sp = 0
for ch in s:
    if ch.lower() in "aeiou":
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    elif ch == " ":
        sp += 1

print(f"Vowels: {v}")
print(f"Consonants: {c}")
print(f"Digits: {d}")
print(f"Spaces: {sp}")