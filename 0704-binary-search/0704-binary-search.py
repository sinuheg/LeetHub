class Solution:
    def search(self, arr: List[int], target: int) -> int:
        low = 0
        top = len(arr)-1
        while low <= top:
            mid = (top + low) // 2
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                # pick right side
                low = mid+1
            elif target < arr[mid]:
                # go to left
                top = mid-1
        return -1