
K = int(input())
digits = [int(input()) for _ in range(K)]
ans = []
sum = 0

for i in range(K):
    if digits[i] != 0:
        ans.append(digits[i])
    else:
        ans.pop()

for digit in ans:
    sum += digit

print(sum)
