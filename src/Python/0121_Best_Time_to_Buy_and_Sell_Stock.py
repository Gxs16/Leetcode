class Solution:
    def maxProfit(self, prices) -> int:
        buy = prices[0]
        sell = 0
        for i in prices:
            buy = min(i, buy)
            sell = max(i-buy, sell)
        return sell