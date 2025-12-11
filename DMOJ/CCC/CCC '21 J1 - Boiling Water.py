B = int(input())

P = 5 * B - 400

print(P)

if P < 100:
    print("1")
elif P > 100:
    print("-1")
else:
    print("0")