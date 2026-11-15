s = input(f"Enter a string: ")
for ch in set(s):
    print(f"{ch} : {s.count(ch)}")