students = int(input())
firstList = list(map(str, input().split()))
secondList = list(map(str, input().split()))
confirm = {}
quality = "good"

for i in range(students):
    confirm[firstList[i]] = secondList[i]

for i in range(students):
    person = firstList[i]
    partner = secondList[i]
    
    if person == partner:
        quality = "bad"
        break
    
    if confirm[partner] != person:
        quality = "bad"
        break

print(quality)
