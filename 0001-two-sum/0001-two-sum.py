class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i, num in enumerate(nums):
            if num not in freq:
                freq[num] = []
            freq[num].append(i)
        output = []
        for i,num in enumerate(nums):
            diff = target - num
            if diff in freq:
                for index in freq[diff]:
                    if index != i:
                        return [i,index]
        return []
        