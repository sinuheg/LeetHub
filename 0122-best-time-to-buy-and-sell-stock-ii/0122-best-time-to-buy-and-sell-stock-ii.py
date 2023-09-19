class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        total_profit = 0
        profit = 0
        for curr in prices:
            if curr < min:
                min = curr
            new_profit = curr - min
            if new_profit > profit:
                profit = new_profit
            elif new_profit >= 0 and new_profit < profit:
                total_profit += profit
                min = curr
                profit = 0
        return total_profit + profit
        
