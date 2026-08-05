class Solution:
    def findComplement(self, num: int) -> int:
        orgBin = str(bin(num)[2:])
        foo = ''
        for letter in orgBin:
            if letter == '0':
                foo += '1'
            else:
                foo += '0'
        return int(foo, 2)
