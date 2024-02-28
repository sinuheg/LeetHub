class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for curr in prices:
            mini = min(mini, curr)
            profit = max(profit, curr - mini )
        return profit
        