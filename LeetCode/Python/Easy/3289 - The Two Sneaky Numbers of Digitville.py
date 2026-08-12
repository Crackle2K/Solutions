from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        sneaky = []
        for key, value in counts.items():
            if value >= 2:
                sneaky.append(key)

        return sneaky
