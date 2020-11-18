'''
@Author: Xinsheng Guo
@Time: 2020-11-17 23:17
@File: 01.07.Rotate_Matrix_LCCI.py
@Link: https://leetcode-cn.com/problems/zero-matrix-lcci/
@Tag: Array
'''
#%%
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])
        rows = []
        columns = []
        for m, i in enumerate(matrix):
            for n, j in enumerate(i):
                if not j:
                    rows.append(m)
                    columns.append(n)
        for i in set(rows):
            matrix[i] = [0]*N
        for j in set(columns):
            for row in matrix:
                row[j] = 0

matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
matrix = [[0,0,0,5],
          [4,3,1,4],
          [0,1,1,4],
          [1,2,1,3],
          [0,0,1,1]]
#%%
S = Solution()
S.setZeroes(matrix)
print(matrix)

