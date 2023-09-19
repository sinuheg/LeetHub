class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert = 0
        read = 0
        while read < len(nums):
            if nums[insert] != nums[read]:
                insert += 1
                nums[insert] = nums[read]
            read += 1
        return insert + 1