class Solution:
    def findMin(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        left = 0
        right = len(arr)-1
        if arr[left] < arr[right]:
            return arr[left]
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and arr[mid-1] > arr[mid]:
                return arr[mid]
            elif mid<len(arr)-1 and arr[mid] > arr[mid+1]:
                return arr[mid+1]
            elif arr[mid] < arr[left]:
                right = mid-1
            else:
                left = mid+1