class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for i in range(m)]

        for i in range(n):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, m):
            dp[i][0] = min(dp[i-1][1], dp[i-1][0])+matrix[i][0]
            for j in range(1, n-1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])+matrix[i][j]
            dp[i][-1] = min(dp[i-1][-1], dp[i-1][-2])+matrix[i][-1]
        return min(dp[-1])