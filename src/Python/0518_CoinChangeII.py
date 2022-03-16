class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1]+[0]*amount
        for j in coins:
            for i in range(j, amount+1):
                dp[i] += dp[i-j]
        return dp[-1]
