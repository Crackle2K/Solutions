
notChanged = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
sign = input().strip()
valid = True

for letter in sign:
    if letter in notChanged:
        pass
    else:
        valid = False

if valid:
    print("YES")
else:
    print("NO")
