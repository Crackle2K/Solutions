
happy, sad = ":-)", ":-("
line = input().strip()
happyCount, sadCount = line.count(happy), line.count(sad)

if happyCount == 0 and sadCount == 0:
    print("none")
else:
    if happyCount > sadCount:
        print("happy")
    elif sadCount > happyCount:
        print("sad")
    else:
        print("unsure")
