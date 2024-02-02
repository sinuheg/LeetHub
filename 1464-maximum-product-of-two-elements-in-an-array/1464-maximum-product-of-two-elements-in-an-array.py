import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            nums[i] = -num
        heapq.heapify(nums)
        return (heapq.heappop(nums)*-1-1) * (heapq.heappop(nums)*-1-1)
        