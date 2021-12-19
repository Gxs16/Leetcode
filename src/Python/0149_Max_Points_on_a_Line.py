'''
@Author: Xinsheng Guo
@Time: 2021年1月28日15:28:38
@File: 0149_Max_Points_on_a_Line.py
@Link: https://leetcode-cn.com/problems/max-points-on-a-line/
@Tag: Hash Table; Math
'''
#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
#%%
# @lc code=start
class Solution:
    def maxPoints(self, points):
        res = 0
        if not points:
            return res
        for i in range(len(points)):
            dic = {}
            same = 0
            curMax = 0
            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    same += 1
                    continue
                if (points[i][0] - points[j][0]) == 0:
                    rate = float('inf')
                else:
                    rate = (points[i][1] - points[j][1]) * 1000000 / (points[i][0] - points[j][0])
                dic[rate] = dic.get(rate, 0) + 1
                curMax = max(curMax, dic[rate])
            res = max(res, curMax+same+1)
        return res
# @lc code=end

# %%
Solution().maxPoints([[0,0],[94911151,94911150],[94911152,94911151]])

#%%
points = [[1,2],[1,2]]
id(points[1])
# %%
id(points[0])