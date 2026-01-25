
def main():
    N  = int(input())
    scored = []
    fouls = []
    starPlayers = 0

    for i in range(N):
        currentScore = int(input())
        scored.append(currentScore)
        currentFouls = int(input())
        fouls.append(currentFouls)

    for i in range(len(scored)):
        if (scored[i] * 5) - (fouls[i] * 3) > 40:
            starPlayers += 1

    if starPlayers == N:
        print(f"{starPlayers}+")
    else:
        print(starPlayers)

if __name__ == '__main__':
    main()
