class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        inter = set(nums1).intersection(set(nums2))
        result = []
        count = 0
        for num in nums1:
            if num in inter:
                count += 1
        result.append(count)
        count = 0
        for num in nums2:
            if num in inter:
                count += 1
        result.append(count)
        
        return result
        