class Solution:
    def canJump(self, nums: List[int]) -> bool:

        """
        table = []
        table = [False] * len(nums)

        table[0] = True

        if nums[0] == 0 and len(nums) != 1:
            return False

        for i in range(len(nums)):
            
            if table[i]:            
            
            
                # check which future squares are reachable


                for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                    table[j] = True


        if table[len(nums) - 1] == True:
            return True
        else:
            return False
        """
        
        r = 0
        for i in range(len(nums)):            

            if i > r:
                return False

            if r >= len(nums) - 1:
                return True

            if i + nums[i] > r:
                r = i + nums[i]

        return False


