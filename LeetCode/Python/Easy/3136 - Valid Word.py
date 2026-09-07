class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) >= 3:
            vowels = ['a', 'e', 'i', 'o', 'u',]
            consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

            hasVowel, hasConst = False, False
            if word.isalnum():
                for character in word.lower():
                    if character in vowels:
                        hasVowel = True
                    if character in consonants:
                        hasConst = True
            
                if hasConst == True and hasVowel == True:
                    return True
        
        return False
