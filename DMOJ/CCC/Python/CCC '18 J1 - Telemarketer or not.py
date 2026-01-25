def main():

    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

    if (num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num3):
        print("ignore")
    else:
        print("answer")

main()