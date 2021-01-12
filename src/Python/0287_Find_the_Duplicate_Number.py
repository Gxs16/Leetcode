'''
@Author: Xinsheng Guo
@Time: 2021年1月12日17:52:52
@File: 0287_Find_the_Duplicate_Number.py
@Link: https://leetcode-cn.com/problems/find-the-duplicate-number/
@Tag: Array; Two Pointers; Binary Search
'''
#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
#%%
# @lc code=start
class Solution:
    def findDuplicate(self, nums) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
# @lc code=end

#%%
Solution().findDuplicate([1,3,4,2,2])
# %%
