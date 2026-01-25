def main():

    limit = int(input())
    carSpeed = int(input())

    exceed = carSpeed - limit

    if carSpeed <= limit:
        print("Congratulations, you are within the speed limit!")
    elif exceed <= 20:
        print("You are speeding and your fine is $100.")
    elif exceed <= 30:
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $500.")


main()