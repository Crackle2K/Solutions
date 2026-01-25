
N = int(input())
days = [input() for _ in range(N)]

left = 0
rain = 0
ans = 0

for right in range(N):
    if days[right] == "P":
        rain += 1

    while rain > 1:
        if days[left] == "P":
            rain -= 1
        left += 1

    ans = max(ans, right - left + 1)

if 'P' not in days:
    ans -= 1

print(ans)
