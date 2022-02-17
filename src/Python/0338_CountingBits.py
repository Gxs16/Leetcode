class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        else:
            dp = [0] * (n+1)
            dp[1] = 1
            for i in range(n+1):
                dp[i] = dp[i//2]+dp[i%2]
            return dp
