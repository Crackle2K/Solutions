
N = int(input())
line2 = input()
line3 = input()
similarities = 0

for i in range(N):
    if line2[i] == 'C':
        if line2[i] == line3[i]:
            similarities += 1
        else:
            pass

print(similarities)
