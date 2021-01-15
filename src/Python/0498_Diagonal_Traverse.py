'''
@Author: Xinsheng Guo
@Time: 2020-11-29 18:13:34
@File: 0498_Diagonal_Traverse.py
@Link: https://leetcode-cn.com/problems/diagonal-traverse/
@Tag: Depth-first Search; Dynamic Programming
'''
#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#
#%%
# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix):
        result = []
        if not matrix:
            return result
        lenth_x = len(matrix)
        lenth_y = len(matrix[0])
        reverse = False
        for i in range(lenth_x+lenth_y-1):
            if reverse:
                for x in range(max(0, i-lenth_y+1), min(i+1, lenth_x)):
                    result.append(matrix[x][i-x])
                reverse = False
            else:
                for y in range(max(0, i-lenth_x+1), min(i+1, lenth_y)):
                    result.append(matrix[i-y][y])
                reverse = True
        return result
# @lc code=end
#%%
Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
# %%
