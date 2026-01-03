
def main():
    P = int(input())
    N = int(input())
    R = int(input())

    day = 0
    total = N
    infected = N

    while total <= P:
        day += 1
        infected *= R
        total += infected

    print(day)

if __name__ == '__main__':
    main()
