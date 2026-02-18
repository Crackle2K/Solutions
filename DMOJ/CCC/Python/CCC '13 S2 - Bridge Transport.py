
maxWeight, N = int(input()), int(input())
carweights = [int(input()) for _ in range(N)]
currentWeight, count = 0, 0

for i in range(N):
    currentWeight += carweights[i]
    if i >= 4:
        currentWeight -= carweights[i - 4]

    if currentWeight > maxWeight:
        break
    
    count += 1


print(count)
