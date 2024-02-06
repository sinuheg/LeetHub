class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        middle = total_len // 2
        n1 = 0
        n2 = 0
        count = 0
        last = None
        result = []
        while (n1 < len(nums1) or n2 < len(nums2)) and len(result) < 2:
            if n1 < len(nums1) and n2 < len(nums2):
                if nums1[n1] <= nums2[n2]:
                    last = nums1[n1]
                    n1 += 1
                    count += 1
                else:
                    last = nums2[n2]
                    n2 += 1
                    count += 1
            else:
                if n1 < len(nums1):
                    last = nums1[n1]
                    n1 += 1
                    count += 1
                else: 
                    last = nums2[n2]
                    n2 += 1
                    count += 1
            if count >= middle:
                result.append(last)
        if total_len % 2 == 1:
            return result[-1]
        else:
            return (result[0] + result[1])/2 if len(result)> 1 else result[-1]
