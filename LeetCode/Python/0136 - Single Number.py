class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for item in counts:
            if counts[item] == 1:
                single = item

        return single
