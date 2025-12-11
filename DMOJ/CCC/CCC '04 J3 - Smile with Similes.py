def main():

    n = int(input())
    m = int(input())

    adjectives = []
    for i in range(n):
        adj = input().strip()
        adjectives.append(adj)
    
    nouns = []
    for i in range(m):
        noun = input().strip()
        nouns.append(noun)

    for adjective in adjectives:
        for noun in nouns:
            print(f"{adjective} as {noun}")


main() 