from functools import cache


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0]*n for i in range(n)]
        for l in range(2, n):
            for i in range(0, n-l):
                j = i+l
                res = float('inf')
                for k in range(i+1, j):
                    res = min(res, dp[i][k]+values[k]*values[j]*values[i]+dp[k][j])
                dp[i][j] = res
        return dp[0][n-1]

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(i, j):
            res = 100000000
            for k in range(i + 1, j):
                res = min(res, dp(i, k) + dp(k, j) + values[i] * values[j] * values[k])
            return res%100000000

        return dp(0, len(values) - 1)