'''
@Author: Xinsheng Guo
@Time: 2021年1月26日11:39:30
@File: 0454_4Sum_II.py
@Link: https://leetcode-cn.com/problems/4sum-ii/
@Tag: Hash Table; Binary Search
'''
#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
'''class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        result = 0
        CD_dict = {}
        for i in C:
            for j in D:
                if i+j in CD_dict:
                    CD_dict[i+j] += 1
                else:
                    CD_dict[i+j] = 1
        for i in A:
            for j in B:
                if 0-(i+j) in CD_dict:
                    result += CD_dict[0-(i+j)]
        return result'''
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        countAB = collections.Counter(u + v for u in A for v in B)
        ans = 0
        for u in C:
            for v in D:
                if -u - v in countAB:
                    ans += countAB[-u - v]
        return ans

# @lc code=end

