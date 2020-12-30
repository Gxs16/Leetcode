'''
@Author: Xinsheng Guo
@Time: 2020-12-21 15:44:11
@File: 0219_Contains_Duplicate_II.py
@Link: https://leetcode-cn.com/problems/contains-duplicate-ii/
@Tag: Design; Hash Map
'''
#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_dict = dict()
        for i, j in enumerate(nums):
            if j in index_dict and (i-index_dict[j]) <= k:
                return True
            else:
                index_dict[j] = i
        return False
# @lc code=end

