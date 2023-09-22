class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        accumulated = []
        running = 1
        for num in nums:
            accumulated.append(running)
            running *= num
        running = 1
        i = len(nums)-1
        while i >= 0:
            accumulated[i] *= running
            running *= nums[i]
            i -= 1
        return accumulated
        