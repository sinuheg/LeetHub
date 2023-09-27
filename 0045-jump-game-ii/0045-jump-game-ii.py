class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return -1
        dp = [0] * len(nums)
        i = len(nums) - 2
        while i >= 0:
            jum = nums[i]
            mini = dp[i + 1]
            j = 1
            while j <= jum and i+j < len(dp):
                mini = min(mini, dp[i+j])
                j += 1
            dp[i] = mini + 1
            i -= 1
        return dp[0]
        
        