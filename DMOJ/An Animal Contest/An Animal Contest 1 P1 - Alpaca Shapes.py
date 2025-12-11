import math

lines = input()
S, R = lines.split()
S = int(S)
R = int(R)

totalSquare = S * S
totalCircle = math.pi * (R * R)

if totalSquare > totalCircle:
    print("SQUARE")
else:
    print("CIRCLE")