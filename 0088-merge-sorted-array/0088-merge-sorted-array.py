class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        insert = n + m - 1
        n -= 1
        m -= 1
        while n >= 0 and m >= 0:
            if nums1[m] > nums2[n]:
                nums1[insert] = nums1[m]
                insert -= 1
                m -= 1
            elif nums1[m] < nums2[n]:
                nums1[insert] = nums2[n]
                insert -= 1
                n -= 1
            else:
                nums1[insert] = nums1[m]
                insert -= 1
                m -= 1
                nums1[insert] = nums2[n]
                insert -= 1
                n -= 1
        
        while n >= 0:
            nums1[insert] = nums2[n]
            insert -= 1
            n -= 1
    