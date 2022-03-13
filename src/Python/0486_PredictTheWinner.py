class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for i in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]
    
        for d in range(1, n):
            for i in range(0, n-d):
                j = i+d
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        if dp[0][n-1] >= 0:
            return True
        else:
            return False