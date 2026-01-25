
N = int(input())

student = []
key = []

def count(guesses, correct):
    woah = sum(1 for s, k in zip(guesses, correct) if s == k )
    return woah

for _ in range(N):
    choice = input().strip()
    student.append(choice)

for _ in range(N):
    answer = input().strip()
    key.append(answer)

final = count(student, key)
print(final)
