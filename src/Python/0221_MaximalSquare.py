class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*(n+1) for i in range(m+1)]
        result = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j])+1
                    result = max(result, dp[i+1][j+1])
                else:
                    dp[i+1][j+1] = 0
        return result*result