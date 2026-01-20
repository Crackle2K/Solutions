class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        x = len(words[-1])
        return x
