def main():
    a = int(input())
    b = int(input())
    c = int(input())

    check1 = a == b
    check2 = b == c
    check3 = c == a

    if a + b + c == 180:

        if a == b == c:
            print("Equilateral")
        elif (a == b != c) or (a == c != b) or (b == c != a):
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Error")

main()