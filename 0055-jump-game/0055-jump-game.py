class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_true = len(nums) - 1
        curr = last_true - 1
        while curr >= 0:
            if curr + nums[curr] >= last_true:
                last_true = curr
            curr -= 1
        return last_true == 0
        