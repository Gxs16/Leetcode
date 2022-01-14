class Solution:
    def maxProfit(self, prices) -> int:
        buy = 10**9
        sell = 0
        for i in prices:
            buy = min(i, buy)
            sell = max(i-buy, sell)
        return sell