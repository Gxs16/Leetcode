'''
@Author: Xinsheng Guo
@Time: 2020-11-12 22:26
@File: 0027_Remove_Element.py
@Link: https://leetcode-cn.com/problems/remove-element/
@Tag: Array; Two Pointers
'''
#%%
class Solution:
    def removeElement(self, nums, val: int) -> int:
        right = len(nums)-1
        left = 0
        while right >= left:
            if nums[right] == val:
                right -= 1
            elif nums[left] == val:
                nums[left] = nums[right]
                left += 1
                right -= 1
            else:
                left += 1
        return right+1