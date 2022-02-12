class Solution:
    def rob(self, nums) -> int:
        if len(nums) >= 3:
            dp = [0] * len(nums)
            for i in range(len(nums)):
                dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
            return max(dp[-1], dp[-2])
        else:
            return max(nums)