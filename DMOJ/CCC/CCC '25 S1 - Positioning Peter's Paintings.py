inp = input().split(" ")
a = int(inp[0])
b = int(inp[1])
x = int(inp[2])
y = int(inp[3])

def stacked(a, b, x, y):
    base = max(a, x)
    height = b + y
    p = base * 2 + height * 2
    return p
    
def side_by_side(a, b, x, y):
    base = a + x
    height = max(b, y)
    p = base * 2 + height * 2
    return p

print(min(stacked(a, b, x, y), side_by_side(a, b, x, y)))
