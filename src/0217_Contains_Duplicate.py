'''
@Author: Xinsheng Guo
@Time: 2020-12-18 17:31:54
@File: 0217_Contains_Duplicate.py
@Link: https://leetcode-cn.com/problems/contains-duplicate/
@Tag: Design; Hash Map
'''

class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
Solution().containsDuplicate([1,2,3,1])