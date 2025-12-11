def main():

    spice = {
        "Poblano": 1500,
        "Mirasol": 6000,
        "Serrano": 15500,
        "Cayenne": 40000,
        "Thai": 75000,
        "Habanero": 125000
    }

    n = int(input())
    

    total = 0
    for i in range (n):
        pepper = input().strip()
        total += spice[pepper]

    print(total)

main()
