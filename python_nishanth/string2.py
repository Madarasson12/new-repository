char = {};
name = input("Enter your name:")

for c in name:
    if not c in  char:
        char[c] = 1
    else:
        char[c] += 1
print("Character counts:", char)