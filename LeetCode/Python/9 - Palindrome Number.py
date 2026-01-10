class Solution:
    def isPalindrome(self, x: int) -> bool:
        right = len(str(x)) - 1
        s = str(x)

        for left in range(len(s)):
            if s[left] != s[right]:
                return False
            right -= 1

        return True 
