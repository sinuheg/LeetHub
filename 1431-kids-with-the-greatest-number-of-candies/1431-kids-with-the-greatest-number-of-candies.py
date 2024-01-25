class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = []
        for candy_count in candies:
            result.append(candy_count + extraCandies >= maximum)
        return result
        