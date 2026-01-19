class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        evilT = t[::-1]
        if len(s) == len(t):
            for letter in s:
                if s.count(letter) == evilT.count(letter):
                    pass
                else:
                    return False
            return True
        else:
            return False
