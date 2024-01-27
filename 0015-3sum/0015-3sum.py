class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def search(left, right, target):
            result = []
            while left < right:
                summ = nums[left] + nums[right]
                if summ == target:
                    result.append([nums[left], nums[right]])
                    left+=1
                    right-=1
                elif summ > target:
                    right -= 1
                else:
                    left += 1
            return result
        output = set()
        nums.sort()
        for i,num in enumerate(nums):
            tuples = search(i+1, len(nums)-1, -num)
            for tuplee in tuples:
                output.add((num, *tuplee))
        return list(output)
"""
[-2,-1,0,1,2,3]

"""