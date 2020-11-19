'''
@Author: Xinsheng Guo
@Time: 2020-11-15 16:33
@File: LCCI_01.07.Rotate_Matrix.py
@Link: https://leetcode-cn.com/problems/rotate-matrix-lcci/
@Tag: Array
'''
'''
Given matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

Rotate the matrix in place. It becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
Given matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

Rotate the matrix in place. It becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
'''

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N//2):
            matrix[i], matrix[N-i-1] = matrix[N-i-1], matrix[i]
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
