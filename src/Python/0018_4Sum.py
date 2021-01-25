'''
@Author: Xinsheng Guo
@Time: 2021年1月25日14:36:45
@File: 0018_4Sum.py
@Link: https://leetcode-cn.com/problems/4sum/
@Tag: Array; Two Pointers
'''
#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
#%%
# @lc code=start
class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        result = []
        length = len(nums)
        for i in range(length-3):
            if nums[i] == nums[i-1] and i > 0:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[length-3] + nums[length-2] + nums[length-1] < target:
                continue
            for j in range(i+1, length-2):
                if nums[j] == nums[j-1] and j > i+1:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[length-2] + nums[length-1] < target:
                    continue
                _target = target-nums[i]-nums[j]
                k = j + 1
                l = length-1
                while l > k:
                    total = nums[k]+nums[l]
                    if total == _target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while nums[k] == nums[k-1] and l>k:
                            k += 1
                        l -= 1
                        while nums[l] == nums[l+1] and l>k:
                            l -= 1
                    elif total > _target:
                        l -= 1
                    elif total < _target:
                        k += 1
        return result

# @lc code=end
#%%
Solution().fourSum([-2,-1,-1,1,1,2,2], 0)

# %%
