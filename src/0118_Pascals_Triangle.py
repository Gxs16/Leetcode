'''
@Author: Xinsheng Guo
@Time: 2020年12月25日11:26:40
@File: 0118_Pascals_Triangle.py
@Link: https://leetcode-cn.com/problems/pascals-triangle/
@Tag: Array
'''
#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
#%%
# @lc code=start
class Solution:
    def generate_next_line(self, result, numRows):
        _result = [1]
        for i in range(len(result[-1])-1):
            _result.append(result[-1][i]+result[-1][i+1])
        _result.append(1)
        result.append(_result)
        if numRows > 1:
            result = self.generate_next_line(result, numRows-1)
        return result
            
    def generate(self, numRows: int):
        if numRows >= 2:
            result = [[1]]
            return self.generate_next_line(result, numRows-1)
        elif numRows == 1:
            return [[1]]
        else:
            return []
            
# @lc code=end
#%%
Solution().generate(1)

# %%
