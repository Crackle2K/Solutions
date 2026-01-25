square_list = []
for _ in range(3):
    row = input().split()
    square_list.append(row)

for i in range(3):
    for j in range(3):
        if square_list[i][j] != 'X':
            square_list[i][j] = int(square_list[i][j])


def calculate(g):
    distribute(g)
    if full(g) and checker(g):
        for r in g:
            print(*r)
        return True

    for i in range(3):
        for j in range(3):
            if g[i][j] == 'X':
                new = remake(g)
                new[i][j] = 1
                if calculate(new):
                    return True
    return False

def distribute(g):
    changed = True
    while changed:
        changed = False
        for i in range(3):
            a, b, c = deduce(g[i][0], g[i][1], g[i][2])
            
            
            
            
            if a is not None:
                g[i][0], g[i][1], g[i][2] = a, b, c
                changed = True

            a, b, c = deduce(g[0][i], g[1][i], g[2][i])
            if a is not None:
                g[0][i], g[1][i], g[2][i] = a, b, c
                changed = True
    return g

def full(g):
    return all('X' not in r for r in g)

def checker(g):
    def ok(a, b, c):
        return c - b == b - a

    for i in range(3):
        if not ok(g[i][0], g[i][1], g[i][2]):
            return False

    for j in range(3):
        if not ok(g[0][j], g[1][j], g[2][j]):
            return False

    return True

def deduce(a, b, c):
    if a != 'X' and b != 'X' and c != 'X':
        return None, None, None
    if a != 'X' and b != 'X':
        return a, b, b + (b - a)
    if a != 'X' and c != 'X':
        return a, (a + c) // 2, c
    if b != 'X' and c != 'X':
        return b - (c - b), b, c
    return None, None, None

def remake(g):
    return [r[:] for r in g]

calculate(square_list)
