def main():

    n = int(input())

    antonia = 100
    david = 100

    for i in range(n):
        game = input()
        a, d = game.split()
        an, da = int(a), int(d)
        if an < da:
            antonia = antonia - da
        if da < an:
            david = david - an
        
    print(antonia)
    print(david)

main()
