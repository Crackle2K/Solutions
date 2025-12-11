def main():

    game1 = input().strip()
    game2 = input().strip()
    game3 = input().strip()
    game4 = input().strip()
    game5 = input().strip()
    game6 = input().strip()

    history = []

    history.append(game1)
    history.append(game2)
    history.append(game3)
    history.append(game4)
    history.append(game5)
    history.append(game6)

    win = "W"
    loss = "L"

    wins = history.count(win)

    if wins == 0:
        print(-1)
    elif wins == 1 or wins == 2:
        print(3)
    elif wins == 3 or wins == 4:
        print(2)
    else:
        print(1)
    

main()
