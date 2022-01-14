class Solution:
    def maxProfit(self, prices) -> int:
        result = 0
        prices = [prices[0]]+prices+[prices[-1]]
        buy = prices[0]
        for i in range(1, len(prices)-1):
            left = i-1
            right = i+1
            if prices[left] >= prices[i] and prices[right] >= prices[i]:
                buy = prices[i]
            if prices[left] <= prices[i] and prices[right] <= prices[i]:
                result += prices[i]-buy
        return result

class Solution:
    def maxProfit(self, prices) -> int:
        result = 0
        for i in range(len(prices)-1):
            result += max(0, prices[i+1]-prices[i])
        return result