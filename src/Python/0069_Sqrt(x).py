'''
@Author: Xinsheng Guo
@Time: 2021年1月7日10:56:33
@File: 0069_Sqrt(x).py
@Link: https://leetcode-cn.com/problems/sqrtx/
@Tag: Math; Binary Search
'''
#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
#%%
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            x0 = x
            C = x
            error = 1
            while error > 10**(-3):
                xi = 0.5 * (x0 + C / x0)
                error = x0-xi 
                x0 = xi
            return int(xi)
# @lc code=end
#%%
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x+1
        while right > left+1:
            target = (right+left)//2
            if target**2 > x:
                right = target
            elif target**2 < x:
                left = target
            else:
                return target
        return left
# %%