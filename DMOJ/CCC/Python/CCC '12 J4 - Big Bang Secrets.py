
K = int(input())
word = input().strip()

def shift(char, amount):
    newChar = (ord(char) - ord('A') - amount) % 26 + ord('A')
    return chr(newChar)

P = 1
S = 3 * P + K

letters = list(word)
newWord = []

for i in range(len(letters)):
    P = i + 1
    S = 3 * P + K
    newLetter = shift(letters[i], S)
    newWord.append(newLetter)

print(''.join(newWord))
