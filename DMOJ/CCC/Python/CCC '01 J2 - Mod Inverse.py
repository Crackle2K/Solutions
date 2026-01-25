import math

x = int(input())
m = int(input())

def modular_inverse(x, m):
    if math.gcd(x, m) != 1:
        print("No such integer exists.")
        return None

    for n in range(1, m):
        if (x * n) % m == 1:
            return n


result = modular_inverse(x, m)
if result is not None:
    print(result)
