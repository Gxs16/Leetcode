class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        cap = total_sum//2
        if len(nums) <= 1 or max(nums) > cap or total_sum%2 != 0:
            return False
        dp = [[True]*len(nums)]+[[False]*len(nums) for i in range(cap)]
        dp[nums[0]] = [True]*len(nums)
        for j in range(1, len(nums)):
            num = nums[j]
            for i in range(1, num+1):
                dp[i][j] = dp[i][j-1]
            for i in range(num+1, 1+cap):
                dp[i][j] = dp[i-num][j-1] or dp[i][j-1]
                
        return dp[-1][-1]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        cap = total_sum//2
        if len(nums) <= 1 or max(nums) > cap or total_sum%2 != 0:
            return False
        dp = [True]+[False]*cap
        for num in nums:
            for i in range(cap, num-1, -1):
                dp[i] = dp[i-num] or dp[i]
        return dp[-1]
