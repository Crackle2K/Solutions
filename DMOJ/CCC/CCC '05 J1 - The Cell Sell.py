def main():

    daytime = int(input())
    evening = int(input())
    weekend = int(input())
        
    planA = max(0, daytime - 100) * 0.25 + evening * 0.15 + weekend * 0.20
    planB = max(0, daytime - 250) * 0.45 + evening * 0.35 + weekend * 0.25

    roundA = round(planA, 2)
    roundB = round(planB, 2)

    print(f"Plan A costs {roundA:.2f}")
    print(f"Plan B costs {roundB:.2f}")

    centsA = int(roundA * 100)
    centsB = int(roundB * 100)

    if centsA < centsB:
        print("Plan A is cheapest.")
    elif centsB < centsA:
        print("Plan B is cheapest.")
    else:
        print("Plan A and B are the same price.")

main()
