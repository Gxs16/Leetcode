class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i-j >= 0:
                    dp[i] = min(dp[i], dp[i-j]+1)
        if dp[-1]>amount:
            return -1
        else:
            return dp[-1]
