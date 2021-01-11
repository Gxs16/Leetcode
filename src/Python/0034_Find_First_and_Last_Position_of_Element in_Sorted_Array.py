'''
@Author: Xinsheng Guo
@Time: 2021年1月11日13:59:27
@File: 0034_Find_First_and_Last_Position_of_Element_in_Sorted_Array.py
@Link: https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
@Tag: Two Pointers; String
'''
#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
#%%
# @lc code=start
class Solution:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1, -1]
        result = []
        left = 0
        right = len(nums)-1
        while right > left+1:
            mid = left+(right-left)//2
            if nums[mid] < target:
                left = mid
            elif nums[mid] == target:
                right = mid
            else:
                right = mid-1
        if nums[left] == target:
            result.append(left)
        elif nums[right] == target:
            result.append(right)
        else:
            return [-1, -1]

        right = len(nums)-1
        while right > left+1:
            mid = left+(right-left)//2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] == target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            result.append(right)
        elif nums[left] == target:
            result.append(left)
        return result
# @lc code=end
#%%
Solution().searchRange([8,8], 8)

# %%
