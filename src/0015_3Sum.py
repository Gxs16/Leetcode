'''
@Author: Xinsheng Guo
@Time: 2020年12月23日16:57:57
@File: 0015_3Sum.py
@Link: https://leetcode-cn.com/problems/3sum/
@Tag: Array; Two Pointers
'''
#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
#%%
# @lc code=start
class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        i = 0
        while i <= n-2 and nums[i] <= 0:
            while i > 0 and nums[i] == nums[i-1] and i <= n-3:
                i += 1
            k = n-1
            j = i+1
            while j < k:
                while nums[j] + nums[k] + nums[i] > 0 and j < k:
                    k -= 1
                if nums[j] + nums[k] + nums[i] == 0 and j < k:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    while nums[k] == nums[k+1] and j < k:
                        k -= 1
                while nums[j] + nums[k] + nums[i] < 0 and j < k:
                    j += 1
            i += 1
        return result
# @lc code=end
#%%
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
Solution().threeSum(nums)
# %%
nums = [0,0,0,0]
Solution().threeSum(nums)
# %%
nums = [1,2,-2,-1]
Solution().threeSum(nums)