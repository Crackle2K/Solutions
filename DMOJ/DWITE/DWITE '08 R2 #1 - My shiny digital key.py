import sys
from collections import Counter

def main():
    data = sys.stdin.read().strip()
    blocks = data.split("\n\n")
    grids = [block.splitlines() for block in blocks]

    for i in grids:
        myString = ""
        for j in i:
            counts = Counter(j)
            myString += str(counts["#"])

        print(myString)

if __name__ == '__main__':
    main()