def main():

    sentence = input()
    myV = "V"
    myH = "H"

    Vcount = sentence.count(myV)
    Hcount = sentence.count(myH)

    topLeft = int(1)
    topRight = int(2)
    bottomLeft = int(3)
    bottomRight = int(4)

    for i in range(Vcount):
        topRight, topLeft = topLeft, topRight
        bottomLeft, bottomRight = bottomRight, bottomLeft
    for i in range(Hcount):
        topRight, bottomRight = bottomRight, topRight
        topLeft, bottomLeft = bottomLeft, topLeft

    
    print(topLeft, topRight)
    print(bottomLeft, bottomRight)



# ORIGINAL
# 1 2
# 3 4

main()