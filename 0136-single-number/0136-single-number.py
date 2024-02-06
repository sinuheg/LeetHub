"""
3 11
2 01
x 10
3 11
x 01
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]
        return result
        