'''
@Author: Xinsheng Guo
@Time: 2020年12月28日16:14:13
@File: 0119_Pascals_Triangle_II.py
@Link: https://leetcode-cn.com/problems/pascals-triangle-ii/
@Tag: Recursion
'''
#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def generate_next_line(self, result, numRows):
        _result = [1]
        for i in range(len(result)-1):
            _result.append(result[i]+result[i+1])
        _result.append(1)
        if numRows > 1:
            _result = self.generate_next_line(_result, numRows-1)
        return _result
            
    def getRow(self, numRows: int):
        if numRows >= 1:
            result = [1]
            return self.generate_next_line(result, numRows)
        elif numRows == 0:
            return [1]
        else:
            return []
# @lc code=end

