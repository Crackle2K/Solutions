Y = input()
Z = int(Y)
Z += 1

while len(set(str(Z))) != len(str(Z)):
    Z += 1

print(Z)
