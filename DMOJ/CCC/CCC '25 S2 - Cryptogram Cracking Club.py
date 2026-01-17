pattern = input()
c = int(input())

length = 0
i = 0
while i < len(pattern):
    char = pattern[i]
    i += 1
    num = 0
    while i < len(pattern) and pattern[i].isdigit():
        num = num * 10 + int(pattern[i])
        i += 1
    length += num

c = c % length

running = 0
i = 0
while i < len(pattern):
    char = pattern[i]
    i += 1
    num = 0
    while i < len(pattern) and pattern[i].isdigit():
        num = num * 10 + int(pattern[i])
        i += 1
    if running + num > c:
        print(char)
        break
    running += num
