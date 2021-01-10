'''
@Author: Xinsheng Guo
@Time: 2021年1月10日22:17:44
@File: 0153_Find_Minimum_in_Rotated_Sorted_Array.py
@Link: https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
@Tag: Array; Binary Search
'''
#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while right > left+1:
            target = left+(right-left)//2
            if nums[target] > nums[left]:
                left = target
            if nums[target] < nums[right]:
                right = target
        return nums[right]
# @lc code=end

