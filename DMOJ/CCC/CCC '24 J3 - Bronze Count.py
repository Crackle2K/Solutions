
N = int(input())
scores = []

for i in range(N):
    score = int(input())
    scores.append(score)

gold = max(scores)
for i in range(N):
    if scores[i] == gold:
        scores[i] = -1

silver = max(scores)
for i in range(N):
    if scores[i] == silver:
        scores[i] = -1

count = 0
bronze = max(scores)
for i in range(N):
    if scores[i] == bronze:
        count += 1


print(bronze, count)
