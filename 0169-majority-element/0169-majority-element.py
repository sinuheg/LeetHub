class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        start = 0
        end = 0
        count = 0
        while end < len(nums):
            if nums[start] != nums[end]:
                start = end
                count = 1
            else:
                count += 1
                if count >= len(nums)/2:
                    return nums[start]
            end += 1
        return nums[0]