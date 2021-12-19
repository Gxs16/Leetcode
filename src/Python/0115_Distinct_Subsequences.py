class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len = len(s)
        t_len = len(t)
        dp = [[1]*(s_len+1)]+[[0] * (s_len+1) for i in range(t_len)]
        for i, c_t in enumerate(t):
            for j, c_s in enumerate(s):
                if c_t == c_s:
                    dp[i+1][j+1] = dp[i][j] + dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
        return dp[t_len][s_len]