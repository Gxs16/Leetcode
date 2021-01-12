'''
@Author: Xinsheng Guo
@Time: 2021年1月12日10:48:36
@File: 0154_Find_Minimum_in_Rotated_Sorted_Array_II.py
@Link: https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
@Tag: Array; Binary Search
'''
#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
#%%
# @lc code=start
class Solution:
    def findMin(self, nums) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        else:
            left = 0
            right = len(nums)-1
            while right > left+1:
                mid = left+(right-left)//2
                if nums[mid] == nums[left] and nums[right] == nums[left]:
                    if nums[mid]*(right-mid) == sum(nums[mid:right]):
                        right = mid
                    else:
                        left = mid
                elif nums[mid] >= nums[left]:
                    left = mid
                elif nums[mid] <= nums[right]:
                    right = mid
            return nums[right]

# @lc code=end
#%%
Solution().findMin([1,3,1,1])

# %%
