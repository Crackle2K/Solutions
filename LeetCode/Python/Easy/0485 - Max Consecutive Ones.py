class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        scores = []
        foo = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                foo += 1
            else:
                scores.append(foo)
                foo = 0
        scores.append(foo)
        highest = max(scores)
        return highest
