
def shift(number):
    return (number * 10)

N = int(input())
k = int(input())

total = N
current = N

for i in range(k): 
    current = shift(current)
    total += current


print(total)
