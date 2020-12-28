'''
@Author: Xinsheng Guo
@Time: 2020年12月28日17:55:41
@File: 0509_Fibonacci_Number.py
@Link: https://leetcode-cn.com/problems/fibonacci-number/
@Tag: Array
'''
#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def get_fib(self, n: int, record: dict) -> int:
        if not n-2 in record:
            record[n-2] = self.get_fib(n-2, record)
        if not n-1 in record:
            record[n-1] = self.get_fib(n-1, record)
        return record[n-1]+record[n-2]

    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            record = {0:0, 1:1}
            return self.get_fib(n, record)
# @lc code=end

