'''
 0 1 2 3 4
[1,3,4,2,2]

1 -> 3 -> 2 -> 4 -> 2 
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[0]
        slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
        