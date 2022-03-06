class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[True]*n for i in range(n)]
        result = n
        for k in range(1, n):
            for i in range(0, n-k):
                j = i+k
                if s[i] == s[j] and dp[i+1][j-1]:
                    result += 1
                else:
                    dp[i][j] = False
        return result
