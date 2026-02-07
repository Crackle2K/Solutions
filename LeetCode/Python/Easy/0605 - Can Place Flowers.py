class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowercheck = [0] + flowerbed + [0]
        for i in range(1, len(flowercheck) - 1):
            if flowercheck[i] == 0 and flowercheck[i - 1] == 0 and flowercheck[i + 1] == 0:
                flowercheck[i] = 1
                n -= 1
        
        if n <= 0:
            return True
        else:
            return False
