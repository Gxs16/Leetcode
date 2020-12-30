'''
@Author: Xinsheng Guo
@Time: 2020-12-3 22:20:30
@File: 0200_Number_of_Islands.py
@Link: https://leetcode-cn.com/problems/number-of-islands/
@Tag: Array; Sort
'''
#%%
from queue import Queue
class Solution:
    def numIslands(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        bfs = Queue()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    bfs.put((i, j))
                    count += 1
                    while not bfs.empty():
                        x, y = bfs.get()
                        if x-1 >= 0 and grid[x-1][y] == '1':
                            grid[x-1][y] = '0'
                            bfs.put((x-1, y))
                        if y-1 >= 0 and grid[x][y-1] == '1':
                            grid[x][y-1] = '0'
                            bfs.put((x, y-1))
                        if x+1 < m and grid[x+1][y] == '1':
                            grid[x+1][y] = '0'
                            bfs.put((x+1, y))
                        if y+1 < n and grid[x][y+1] == '1':
                            grid[x][y+1] = '0'
                            bfs.put((x, y+1))
        return count
#%%
grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
Solution().numIslands(grid)
# %%
base = (0,0)
grid[base[0]][base[1]]
# %%
