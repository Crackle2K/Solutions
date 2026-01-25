def main():

    N = int(input())
    maxValue = 0
    maxName = ""

    for i in range(N):
        name = input()
        bid = int(input())
        if bid > maxValue:
            maxValue = bid
            maxName = name
        
        

    print(maxName)

main()
