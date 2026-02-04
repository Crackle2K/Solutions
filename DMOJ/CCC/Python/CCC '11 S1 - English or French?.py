from collections import Counter

N = int(input())
texts = []
for i in range(N):
    text = input()
    texts.append(text)

joined = "".join(texts).lower()

allCounts = Counter(joined)

tCount = allCounts['t']
sCount = allCounts['s']


if tCount > sCount:
    print("English")
elif tCount < sCount:
    print("French")
else:
    print("French")
