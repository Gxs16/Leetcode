class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i][j+1]+dp[i+1][j]+mat[i][j]-dp[i][j]
        
        res = [[0]*(n) for i in range(m)]
        for i in range(m):
            for j in range(n):
                right = min(n-1, j+k)
                left = max(0, j-k)
                top = max(0, i-k)
                down = min(i+k, m-1)
                res[i][j] = dp[down+1][right+1]+dp[top][left]-dp[down+1][left]-dp[top][right+1]
        return res