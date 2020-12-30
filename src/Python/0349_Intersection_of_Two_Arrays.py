'''
@Author: Xinsheng Guo
@Time: 2020-12-18 17:59:01
@File: 0349_Intersection_of_Two_Arrays.py
@Link: https://leetcode-cn.com/problems/intersection-of-two-arrays/submissions/
@Tag: Queue
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))
