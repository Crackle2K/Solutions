def main():

    H = int(input())
    S = int(input())
    Q = int(input())

    for i in range(Q):
        H -= S
        print(H)


main()