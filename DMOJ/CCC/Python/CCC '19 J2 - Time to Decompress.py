
L = int(input())
lines = []

for i in range(L):
    foo = input()
    lines.append(foo)

for line in lines:
    symbol = line[-1]
    if line[1] == ' ':
        value = int(line[0])
        print(symbol * value)
    else:
        digits = f"{line[0]}{line[1]}"
        value = int(digits)
        print(symbol * value)
