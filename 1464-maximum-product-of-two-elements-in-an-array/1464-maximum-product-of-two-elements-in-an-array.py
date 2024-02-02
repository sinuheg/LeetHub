import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        largest = heapq.nlargest(2, nums)
        return (largest[0]-1) * (largest[1]-1)
        