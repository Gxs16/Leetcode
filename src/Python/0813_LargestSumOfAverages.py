class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp = [[0]*k for i in range(len(nums))]
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            dp[i][0] = total_sum/(i+1)

        for j in range(1, k):
            for i in range(j, len(nums)):
                total_sum = sum(nums[j:i+1])
                for l in range(j-1, i):
                    dp[i][j] = max((dp[l][j-1]+(total_sum-nums[l])/(i-l)), dp[i][j])
        return dp[len(nums)-1][k-1]
