def main():

    tineHeight = int(input())
    space = int(input())
    handle = int(input())


    for i in range(tineHeight):
        print('*' + ' ' * space + '*' + ' ' * space + '*')

    print('*' * (3 + 2 * space))

    for i in range(handle):
        print(' ' * (1 + space) + '*')


main()
