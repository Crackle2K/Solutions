
T, C = int(input()), int(input())
chores = [int(input()) for _ in range(C)]
chores.sort()
possible = 0

for i in range(C):
    T -= chores[i]
    if T >= 0:
        possible += 1

print(possible)
