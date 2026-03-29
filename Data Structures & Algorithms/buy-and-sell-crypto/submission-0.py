class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxProfit = 0
        Buy = prices[0]

        for Sell in prices:
            Buy = min(Buy, Sell)
            MaxProfit = max(MaxProfit, Sell - Buy)

        return MaxProfit