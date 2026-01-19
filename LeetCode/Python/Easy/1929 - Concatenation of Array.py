class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        firstList, secondList = nums, nums
        firstList.extend(secondList)
        return firstList
