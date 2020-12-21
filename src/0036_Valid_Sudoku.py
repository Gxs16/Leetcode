'''
@Author: Xinsheng Guo
@Time: 2020年12月21日17:27:55
@File: 0036_Valid_Sudoku.py
@Link: https://leetcode-cn.com/problems/valid-sudoku/
@Tag: Hash Table
'''
# 0036_Valid_Sudoku.py
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
#%%
# @lc code=start
class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in board:
            check_list = []
            for j in i:
                if j in check_list:
                    return False
                elif not j in check_list and j != '.':
                    check_list.append(j)
        for i in range(9):
            check_list = []
            for j in range(9):
                if board[j][i] in check_list:
                    return False
                elif not board[j][i] in check_list and board[j][i] != '.':
                    check_list.append(board[j][i])
        for i in range(3):
            alpha = 3*i
            for j in range(3):
                beta = 3*j
                check_list = []
                for k in range(3):
                    for l in range(3):
                        if board[alpha+k][beta+l] in check_list:
                            return False
                        elif not board[alpha+k][beta+l] in check_list and board[alpha+k][beta+l] != '.':
                            check_list.append(board[alpha+k][beta+l])
        return True
# @lc code=end
#%%
a = \
[[".", ".", ".", ".", "5", ".", ".", "1", "."],
 [".", "4", ".", "3", ".", ".", ".", ".", "."],
 [".", ".", ".", ".", ".", "3", ".", ".", "1"],
 ["8", ".", ".", ".", ".", ".", ".", "2", "."],
 [".", ".", "2", ".", "7", ".", ".", ".", "."],
 [".", "1", "5", ".", ".", ".", ".", ".", "."],
 [".", ".", ".", ".", ".", "2", ".", ".", "."],
 [".", "2", ".", "9", ".", ".", ".", ".", "."],
 [".", ".", "4", ".", ".", ".", ".", ".", "."]]
Solution().isValidSudoku(a)

# %%
