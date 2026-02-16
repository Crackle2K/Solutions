class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        if x[-1] == '-':
            x = x[:-1]
            x = '-' + x
        if int(x) > (2 ** 31) - 1:
            return 0
        elif int(x) < -((2 ** 31) - 1):
            return 0
        else:
            return int(x)
