
s, w = int(input()), int(input())
timeSleep = (24 - s) + w

if (s >= 20) and (s <= 23):
    if (w >= 6) and (w <= 9):
        if (timeSleep >= 8) and (timeSleep <= 10):
            print("Healthy")
        else: 
            print("Unhealthy")
    else:
        print("Unhealthy")
else: 
    print("Unhealthy")
