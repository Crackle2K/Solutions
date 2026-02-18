
n = int(input())
nums = [int(input()) for _ in range(n)]

for i in range(n):
    divisors = []
    for j in range(1, nums[i]):
        if nums[i] % j == 0:
            divisors.append(j)
    sum = 0
    for num in divisors:
        sum += num
    if sum > nums[i]:
        print(f"{nums[i]} is an abundant number.")
    elif sum < nums[i]:
        print(f"{nums[i]} is a deficient number.")
    else:
        print(f"{nums[i]} is a perfect number.")
