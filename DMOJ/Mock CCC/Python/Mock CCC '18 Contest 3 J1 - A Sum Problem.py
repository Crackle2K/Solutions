
N = int(input())
nums = []
count = 0

for i in range(N):
    num = int(input())
    nums.append(num)

for num in nums:
    if num != 0:
        count += num

print(count)
