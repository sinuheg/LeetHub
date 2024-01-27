class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(left, right, diff):
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == diff:
                    return mid
                if diff > numbers[mid]:
                    left = mid+1
                else:
                    right = mid-1
            return -1
        for i, num in enumerate(numbers):
            diff = target - num
            result = binary_search(i+1, len(numbers)-1, diff)
            if result != -1:
                return [i+1, result+1]
        return []