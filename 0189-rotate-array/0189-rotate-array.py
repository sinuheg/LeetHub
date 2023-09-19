class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == 0:
            return
        def mirror(start, end):
            while start < end:
                aux = nums[start]
                nums[start] = nums[end]
                nums[end] = aux
                start += 1
                end -= 1
        mirror(0, len(nums) - k -1)
        mirror(len(nums) - k, len(nums) - 1)
        mirror(0, len(nums) - 1)