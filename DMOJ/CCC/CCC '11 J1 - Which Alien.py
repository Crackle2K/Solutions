def main():

    antennae = int(input())
    eyes = int(input())


    if antennae >= 3 and eyes <= 4:
        print("TroyMartian")
    if antennae <= 6 and eyes >= 2:
        print("VladSaturnian")
    if antennae <= 2 and eyes <= 3:
        print("GraemeMercurian")

main()