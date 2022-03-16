'''
@Author: Xinsheng Guo
@Time: 2020-11-29 18:13:34
@File: 0494_Target_Sum.py
@Link: https://leetcode-cn.com/problems/target-sum/
@Tag: Depth-first Search; Dynamic Programming
'''
#%%
class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        sum_all = sum(nums)
        diff = sum_all - S
        if diff < 0 or diff % 2:
            return 0
        else:
            diff = int(diff/2)
        F = [1] + [0]*diff
        for j in nums:
            for k in range(diff, j-1, -1):
                F[k] += F[k-j]
        return F[-1]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = sum(nums)
        if sums < abs(target):
            return 0
        dp = [[0]*(len(nums)+1) for i in range(sums*2+1)]
        dp[0][0] = 1
        for i in range(1, len(nums)+1):
            num = nums[i-1]
            for j in range(-sums, -sums+num):
                dp[j][i] = dp[j+num][i-1]
            for j in range(-sums+num, sums-num+1):
                dp[j][i] = dp[j-num][i-1]+dp[j+num][i-1]
            for j in range(sums-num+1, sums+1):
                dp[j][i] = dp[j-num][i-1]
            
        return dp[target][-1]