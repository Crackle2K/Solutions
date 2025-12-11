yearX = int(input())
yearY = int(input())

for i in range(yearX, yearY + 1):
    yearZ = i - yearX
    if yearZ %4 == 0 and yearZ %2 == 0 and yearZ %3==0 and yearZ %5==0:
        print('All positions change in year', i)
