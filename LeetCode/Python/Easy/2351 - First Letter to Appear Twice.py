class Solution:
    def repeatedCharacter(self, s: str) -> str:
        new = []
        for letter in s:
            if letter in new:
                return letter
            else:
                new.append(letter)
