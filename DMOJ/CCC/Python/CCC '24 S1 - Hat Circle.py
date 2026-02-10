

N = int(input())
hatNumbers = [input().strip() for _ in range(N)]
count = 0

for i in range(int(N / 2)):
    if hatNumbers[i] == hatNumbers[int(i + N / 2)]:
        count += 1

print(count * 2)
