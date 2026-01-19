class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkSet = set()
        for num in nums:
            if num in checkSet:
                return True
            checkSet.add(num)
        return False
