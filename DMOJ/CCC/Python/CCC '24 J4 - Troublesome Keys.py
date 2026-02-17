keysInputted = input().strip()
keysDisplayed = input().strip()
sillyKey = ""
wrongLetter = ""
quietKey = "-"

candidates = list(set(keysInputted))
candidates.append("-")

for char in candidates:
    if char != "-":
        testInput = keysInputted.replace(char, "")
    else:
        testInput = keysInputted
    
    if len(testInput) == len(keysDisplayed):
        tempSilly = ""
        tempWrong = ""
        possible = True
        
        for i in range(len(testInput)):
            if testInput[i] != keysDisplayed[i]:
                if tempSilly == "":
                    tempSilly = testInput[i]
                    tempWrong = keysDisplayed[i]
                elif testInput[i] != tempSilly or keysDisplayed[i] != tempWrong:
                    possible = False
                    break

        if possible and tempSilly != "":
            sillyKey = tempSilly
            wrongLetter = tempWrong
            quietKey = char
            break

print(f"{sillyKey} {wrongLetter}")
print(f"{quietKey}")
