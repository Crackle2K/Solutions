def main():

    bowl1 = int(input())
    bowl2 = int(input())
    bowl3 = int(input())

    bowls = [bowl1, bowl2, bowl3]

    highestBowl = max(bowls)
    lowestBowl = min(bowls)

    bowls.remove(highestBowl)
    bowls.remove(lowestBowl)

    middle = bowls[0]

    print(middle)

main()
