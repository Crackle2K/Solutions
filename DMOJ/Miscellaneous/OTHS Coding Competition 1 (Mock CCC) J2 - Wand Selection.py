import math

N = int(input())
explosions = []
for i in range(N):
    explosion = int(input())
    explosions.append(explosion)
sum = 0
for explosion in explosions:
    sum += explosion
sum -= max(explosions)
print(math.floor(sum / (N - 1)))
