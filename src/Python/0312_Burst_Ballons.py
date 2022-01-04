class Solution:
    def maxCoins(self, nums) -> int:
        val = [1]+nums+[1]
        dp = [[0]*len(val) for i in range(len(val))]

        for i in range(len(val)-1, -1, -1):
            for j in range(i+2, len(val)):
                rec = 0
                for k in range(i+1, j):
                    rec = max(rec, val[i]*val[k]*val[j]+dp[i][k]+dp[k][j])
                dp[i][j] = rec

        return dp[0][len(val)-1]
                    
                    