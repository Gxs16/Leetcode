'''
@Author: Xinsheng Guo
@Time: 2021年1月8日11:31:44
@File: 0162_Find_Peak_Element.py
@Link: https://leetcode-cn.com/problems/find-peak-element/
@Tag: Binary Search
'''
#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
#%%
# @lc code=start
class Solution:
    def findPeakElement(self, nums) -> int:
        if len(nums)==1:
            return 0
        if nums[1] < nums[0]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        left = 0
        right = len(nums)-1
        while right > left:
            target = left+((right-left)>>1)
            if nums[target]-nums[target-1] > 0:
                left = target+1
            else:
                right = target
        if nums[left] < nums[left-1]:
            return left-1
# @lc code=end
#%%
Solution().findPeakElement([1,3,2,1])
# %%
