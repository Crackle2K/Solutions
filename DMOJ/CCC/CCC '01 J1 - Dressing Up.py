height = int(input())
dots = -1
space = height * 2

for i in range(height):

    if i >= (height+1) / 2:
        dots -= 2
    else:
        dots += 2

    space = (height * 2) - (dots * 2)

    first = "*" * dots
    blank = " " * space
    last = "*" * dots

    print(first + blank + last)
