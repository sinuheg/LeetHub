class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        read = 0
        insert = 0
        while read < len(nums):
            if nums[read] != val:
                nums[insert] = nums[read]
                insert += 1
            read += 1
        return insert
        