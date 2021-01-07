'''
@Author: Xinsheng Guo
@Time: 2021年1月7日15:10:51
@File: 0033_Search_in_Rotated_Sorted_Array.py
@Link: https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
@Tag: Two Pointers; String
'''
#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
#%%
# @lc code=start
class Solution:
    def binary_search(self, nums, left: int, right: int, target: int) -> int:
        while right >= left:
            pos = left+(right-left)//2
            if nums[pos] > target:
                right = pos-1
            elif nums[pos] < target:
                left = pos+1
            else:
                return pos
        return -1

    def search(self, nums, target: int) -> int:
        end = 0
        start = len(nums)-1
        if nums[start] > nums[end]:
            return self.binary_search(nums, 0, start, target)
        else:
            while start > end+1:
                pos = end+(start-end)//2
                if nums[pos] > nums[end]:
                    end = pos
                elif nums[pos] < nums[start]:
                    start = pos
            if target >= nums[0]:
                return self.binary_search(nums, 0, end, target)
            else:
                return self.binary_search(nums, start, len(nums)-1, target)

# @lc code=end
#%%
Solution().search([8, 4, 6, 7], 7)

# %%
