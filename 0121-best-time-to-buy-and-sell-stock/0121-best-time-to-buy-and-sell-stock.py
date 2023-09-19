class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        for curr in prices:
            if curr < min:
                min = curr
            if curr - min > profit:
                profit = curr - min
        return profit
        