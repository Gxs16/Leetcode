'''
@Author: Xinsheng Guo
@Time: 2020-11-15 16:33
@File: 0056_Merge_Intervals.py
@Link: https://leetcode-cn.com/problems/merge-intervals/
@Tag: Sort; Array
'''

class Solution_API:
    '''
    使用python自有排序api
    '''
    def merge(self, intervals):
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
