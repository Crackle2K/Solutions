
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if y1 == y2:
    print("x-axis")
elif x1 == x2:
    print("y-axis")
else:
    print("neither")