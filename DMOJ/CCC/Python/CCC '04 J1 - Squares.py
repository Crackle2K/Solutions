import math

def main():

    tiles = int(input())

    maxSide = int(math.floor(math.sqrt(tiles)))

    print(f"The largest square has side length {maxSide}.")

main()
