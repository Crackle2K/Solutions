class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)):
            if i == (len(s) - 1):
                score += 0
            else:
                score += abs((ord(s[i])) - ord(s[i + 1]))
            

        return score
