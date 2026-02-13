
n = int(input())
words = [input().strip() for _ in range(n)]

for word in words:
    if (len(word)) > 10:
        construct = f"{word[0]}" + f"{(len(word) - 2)}" + f"{word[-1]}"
        print(construct)
    else:
        print(word)
