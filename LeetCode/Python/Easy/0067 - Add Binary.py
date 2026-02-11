class Solution:
    def addBinary(self, a: str, b: str) -> str:
        newa, newb, = int(a, 2), int(b, 2)
        sum = int(newa + newb)
        return bin(sum)[2:]
