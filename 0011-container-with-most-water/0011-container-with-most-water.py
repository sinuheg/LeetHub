class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0
        left = 0
        right = len(heights)-1
        max_capacity = 0
        while left < right:
            capacity = min(heights[left],heights[right]) * (right - left)
            max_capacity = max(max_capacity, capacity)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_capacity