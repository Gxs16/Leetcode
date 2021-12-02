#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
#%%
# @lc code=start
class Solution:
    def update_neighbor(self, matrix, position: tuple, determined, visited):
        if not position in visited:
            visited.append(position)
            _result = []
            if position[0] > 0 and not (position[0]-1, position[1]) in visited:
                if (position[0]-1, position[1]) in determined:
                    _result.append(matrix[position[0]-1][position[1]])
                else:
                    if matrix[position[0]-1][position[1]] == 0:
                        determined.append((position[0]-1, position[1]))
                        return 1
                    else:
                        _result.append(self.update_neighbor(matrix, (position[0]-1, position[1]), determined, visited))
            if position[0] < len(matrix)-1 and not (position[0]+1, position[1]) in visited:
                if (position[0]+1, position[1]) in determined:
                    _result.append(matrix[position[0]+1][position[1]])
                else:
                    if matrix[position[0]+1][position[1]] == 0:
                        determined.append((position[0]+1, position[1]))
                        return 1
                    else:
                        _result.append(self.update_neighbor(matrix, (position[0]+1, position[1]), determined, visited))
            if position[1] > 0 and not (position[0], position[1]-1) in visited:
                if (position[0], position[1]-1) in determined:
                    _result.append(matrix[position[0]][position[1]-1])
                else:
                    if matrix[position[0]][position[1]-1] == 0:
                        determined.append((position[0], position[1]-1))
                        return 1
                    else:
                        _result.append(self.update_neighbor(matrix, (position[0], position[1]-1), determined, visited))
            if position[1] < len(matrix[0])-1 and not (position[0], position[1]+1) in visited:
                if (position[0], position[1]+1) in determined:
                    _result.append(matrix[position[0]][position[1]+1])
                else:
                    if matrix[position[0]][position[1]+1] == 0:
                        determined.append((position[0], position[1]+1))
                        return 1
                    else:
                        _result.append(self.update_neighbor(matrix, (position[0], position[1]+1), determined, visited))
            matrix[position[0]][position[1]] = min(_result)+1
            determined.append(position)
            visited.pop()
            return min(_result)+1

    def updateMatrix(self, matrix):
        determined = []
        visited = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not (i, j) in determined:
                    if matrix[i][j] == 0:
                        determined.append((i, j))
                    else:
                        self.update_neighbor(matrix, (i, j), determined, visited)
        return matrix

                    
# @lc code=end
#%%
Solution().updateMatrix([[1,0,0],[1,1,0],[1,1,1]])
# %%
