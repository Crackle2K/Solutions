
N = int(input())
coords = []

for i in range(N):
    coord = list(map(int, input().split(',')))
    coords.append(coord)

lowestX = 1000
lowestY = 1000
highestX = 0
highestY = 0

for coord in coords:
    if coord[0] < lowestX:
        lowestX = coord[0]
    if coord[-1] < lowestY:
        lowestY = coord[-1]
    if coord[0] > highestX:
        highestX = coord[0]
    if coord[-1] > highestY:
        highestY = coord[-1]

a, b, c, d = (lowestX - 1), (lowestY - 1), (highestX + 1), (highestY + 1)
print(f"{a},{b}")
print(f"{c},{d}")
