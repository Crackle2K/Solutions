class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        largest = 0
        count = Counter(nums)
        for i in count:
            if count[i] > largest:
                largest = count[i]
        for j in count:
            if count[j] == largest:
                return j
