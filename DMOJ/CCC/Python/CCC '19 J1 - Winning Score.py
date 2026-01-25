def main():
    
    aThP = int(input())
    aTwP = int(input())
    aFT = int(input())

    bThP = int(input())
    bTwP = int(input())
    bFT = int(input())

    result = (aThP * 3 + aTwP * 2 + aFT) - (bThP * 3 + bTwP * 2 + bFT)

    if result > 0:
        print("A")
    elif result < 0:
        print("B")
    else:
        print("T")

main()