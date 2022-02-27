class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [1]*(n+1)
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n+1):
            left = 1
            right = i-1
            result = left*right
            while left <= right:
                result = max(result, dp[left]*dp[right])
                left += 1
                right -= 1
            dp[i] = result
        return dp[-1]
#%%
int(9.5)
# %%
