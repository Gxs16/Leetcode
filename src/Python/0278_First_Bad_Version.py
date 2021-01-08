'''
@Author: Xinsheng Guo
@Time: 2021年1月8日10:11:34
@File: 0278_First_Bad_Version.py
@Link: https://leetcode-cn.com/problems/first-bad-version/
@Tag: Binary Search
'''
#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while right > left:
            target = (right-left)//2+left
            if isBadVersion(target):
                right = target
            else:
                left = target+1
        return left
# @lc code=end

