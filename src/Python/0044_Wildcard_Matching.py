class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(n):
            if p[i] == '*':
                dp[i+1][0] = dp[i][0]
                for j in range(m):
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]
            else:
                for j in range(m):
                    if p[i] == s[j] or p[i] == '?':
                        dp[i+1][j+1] = dp[i][j]

        return dp[n][m]