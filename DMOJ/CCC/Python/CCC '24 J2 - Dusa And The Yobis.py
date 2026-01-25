def main():

    D = int(input())
    dubaHere = True

    while dubaHere:
        yobi = int(input())
        if yobi >= D:
            dubaHere = False
        elif yobi < D:
            D = D + yobi 

    print(D)

main()
