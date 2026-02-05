
N = int(input())
days = []

for i in range(N):
    days.append(input())

count = 0
count2 = 0
result = 0

for i in range(N):
    if days[i] == 'P':
        count += 1
    
    while count > 1:
        if days[count2] == "P":
            count -= 1
        count2 += 1

    result = max(result, i - count2 + 1)

if 'P' not in days:
    result -= 1

print(result)
