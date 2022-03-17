class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0]*(n+1)
        if obstacleGrid[0][0] == 0:
            dp[1] = 1
        else:
            dp[1] = 0
        for i in range(2, n+1):
            if obstacleGrid[0][i-1] == 0:
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
        for i in range(1, m):
            for j in range(1, n+1):
                if obstacleGrid[i][j-1]==0:
                    dp[j] += dp[j-1] 
                else:
                    dp[j] = 0
        return dp[n]