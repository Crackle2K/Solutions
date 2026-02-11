class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = map(int, date.split('-'))
        return (str(bin(year)[2:] + '-' + bin(month)[2:] + '-' + bin(day)[2:]))
