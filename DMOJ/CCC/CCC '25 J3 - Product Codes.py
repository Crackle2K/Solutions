
for code in range(int(input())):
    up, total, sign, num = "", 0, 1, ""
    s = input()
    
    for letter in s:
        if letter.isdigit():
            num += letter
        else:
            if num:
                total += sign * int(num)
                num = ""
            if letter in "+-":
                sign = 1 if letter == "+" else -1
            elif letter.isupper():
                up += letter
                sign = 1
            else:
                sign = 1

    if num:
        total += sign * int(num)

    print(up + str(total))
