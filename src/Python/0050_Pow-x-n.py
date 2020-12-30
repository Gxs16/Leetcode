'''
@Author: Xinsheng Guo
@Time: 2020年12月24日11:02:35
@File: 0050_Pow-x-n.py
@Link: https://leetcode-cn.com/problems/powx-n/
@Tag: Math; Binary Search
'''
#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:            
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            result = self.myPow(x, n//2)
            if n%2 == 1:
                return result*result*x
            else:
                return result*result
        elif n == 0:
            return 1
        else:
            return self.myPow(1/x, -n)
# @lc code=end

