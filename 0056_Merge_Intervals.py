'''
@Author: Xinsheng Guo
@Time: 2020-11-15 16:33
@File: 0056_Merge_Intervals.py
@Link: https://leetcode-cn.com/problems/merge-intervals/
@Tag: Sort; Array
'''
import random

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

class Solution:
    '''
    使用自写快排，双指针循环
    '''
    def sort(self, intervals):
        # 选取比较基
        if len(intervals) > 1:
            right = len(intervals)-1
            left = 1
            base = random.randint(0, right)
            intervals[0], intervals[base] = intervals[base], intervals[0]
            while right > left:
                while intervals[right][0] > intervals[0][0]:
                    right -= 1
                while intervals[left][0] < intervals[0][0]:
                    if left < right:
                        left += 1
                    else:
                        break
                if right > left:
                    intervals[left], intervals[right] = intervals[right], intervals[left]
            if intervals[0] > intervals[right]:
                intervals[0], intervals[right] = intervals[right], intervals[0]
            intervals[:right] = self.sort(intervals[:right])
            intervals[right+1:] = self.sort(intervals[right+1:])
        return intervals

    def merge(self, intervals):
        intervals = self.sort(intervals)
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

S = Solution()
intervals=[[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
intervals = S.sort(intervals)
print(intervals)

#%%
intervals=[[3,1],[5,2],[1,1],[0,1],[4,1]]
intervals2 = intervals[0:3]
intervals[0:3][0] = [3,3]
intervals
# %%
