'''
@Author: Xinsheng Guo
@Time: 2021年1月6日10:22:06
@File: 0704_Binary_Search.py
@Link: https://leetcode-cn.com/problems/binary-search/
@Tag: Binary Search
'''
#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
#%%
# @lc code=start
class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums)-1
        while right >= left:
            pos = (right - left)//2+left
            if nums[pos] == target:
                return pos
            elif nums[pos] > target:
                right = pos-1
            else:
                left = pos+1
        return -1
# @lc code=end
#%%
Solution().search([-1,0,3,5,9,12], 9)