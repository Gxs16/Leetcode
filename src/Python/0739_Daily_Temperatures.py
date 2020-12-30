'''
@Author: Xinsheng Guo
@Time: 2020-12-10-15:15:18
@File: 0739_Daily_Temperatures.py
@Link: https://leetcode-cn.com/problems/daily-temperatures/
@Tag: Stack; Hash Table
'''
#%%
from collections import defaultdict
#%%
class Solution:
    def dailyTemperatures(self, T):
        tem_stack = []
        result = [0] * len(T)
        for i, j in enumerate(T):
            while tem_stack and T[tem_stack[-1]] < j:
                x = tem_stack.pop()
                result[x] = i - x
            tem_stack.append(i)
        return result
#%%
Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
# %%
