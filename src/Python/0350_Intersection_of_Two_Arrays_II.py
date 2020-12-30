'''
@Author: Xinsheng Guo
@Time: 2020-12-21 14:52:56
@File: 0350_Intersection_of_Two_Arrays_II.py
@Link: https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/
@Tag: Array
'''
#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set(nums1) & set(nums2)
        dict1 = dict()
        dict2 = dict()
        for i in nums1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in nums2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        result = []
        for i in intersection:
            result.extend(min(dict1[i], dict2[i])*[i])
        return result
# @lc code=end

