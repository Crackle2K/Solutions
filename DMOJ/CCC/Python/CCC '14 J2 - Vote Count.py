def main():

    V = int(input())
    sentence = input()

    myA = "A"
    myB = "B"

    aCount = sentence.count(myA)
    bCount = sentence.count(myB)

    if aCount > bCount:
        print("A")
    elif bCount > aCount:
        print("B")
    else:
        print("Tie")

main()
