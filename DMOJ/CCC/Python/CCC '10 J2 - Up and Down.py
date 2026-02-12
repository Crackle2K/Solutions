
a, b, c, d, s = int(input()), int(input()), int(input()), int(input()), int(input())

def steps(f, r, m):
    total, steps = 0, 0
    while total < m:
        if total + f <= m:
            steps += f
            total += f
        elif total + f > m:
            steps += m - total
            total += m - total
        if total + r <= m:
            steps -= r
            total += r
        elif total + r > m:
            steps -= m - total
            total += m - total
    return steps

if steps(a, b, s) > steps(c, d, s):
    print("Nikky")
elif steps(a, b, s) < steps(c, d, s):
    print("Byron")
else:
    print("Tied")
