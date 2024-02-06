class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            global_max = max(current_sum, global_max)
        return global_max