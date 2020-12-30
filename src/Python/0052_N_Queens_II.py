'''
@Author: Xinsheng Guo
@Time: 2020-10-20 10:30
@File: 0052_N_Queens_II.py
@Link: https://leetcode-cn.com/problems/n-queens-ii/
'''

import copy

class Queens():
    '''
    计算n皇后问题的类
    使用递归的思想，从左至右逐列计算
    '''
    def __init__(self, n: int):
        '''
        n: 棋盘和皇后的个数
        '''
        self._solution = []
        self.n = n
        grid_select = []
        self._max_depth_search(grid_select)

    def _max_depth_search(self, grid_select: list):
        '''
        grid_select: 当前的落子选择
        递归搜索所有的可能落子方式
        '''
        if len(grid_select) == self.n: # 递归的停止条件：如果落子选择的长度已经满足皇后的个数，就返回当前的选择
            self._solution.append(grid_select)
            return self._solution
        else:
            # 计算下一步的可选的网格
            grid_select.reverse()
            grid_not_available = copy.deepcopy(grid_select)
            for i, j in enumerate(grid_select):
                grid_not_available.extend([j-i-1, j+i+1])
            grid_available = set(i for i in range(self.n))-set(grid_not_available)
            grid_select.reverse()

            # 在下一步的所有可选网格中进行递归搜索
            for k in grid_available:
                grid_select_temp = copy.deepcopy(grid_select)
                grid_select_temp.append(k)
                self._max_depth_search(grid_select_temp)

    def get_the_num_of_solutions(self):
        '''
        获得解的个数
        '''
        return len(self._solution)

    def get_solutions(self):
        '''
        获得解的详细情况
        '''
        return self._solution

if __name__ == '__main__':
    Queens_n = Queens(11)
    print(Queens_n.get_the_num_of_solutions())
    #print(Queens_n.get_solutions())
