'''
@Author: Xinsheng Guo
@Time: 2021年1月27日10:59:26
@File: 0447_Number_of_Boomerangs.py
@Link: https://leetcode-cn.com/problems/number-of-boomerangs/
@Tag: Hash Table
'''
#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#

# @lc code=start
class Solution:
    def permutation(self, m, n):
        result = 1
        for i in range(m-n+1, m+1):
            result *= i
        return result

    def numberOfBoomerangs(self, points) -> int:
        result = 0
        for i in points:
            dis_dict = {}
            for j in points:
                _dis = (i[0]-j[0])**2+(i[1]-j[1])**2
                if _dis in dis_dict:
                    dis_dict[_dis] += 1
                else:
                    dis_dict[_dis] = 1
            for k, l in dis_dict.items():
                if l >= 2:
                    result += self.permutation(l, 2)
        return result
# @lc code=end
