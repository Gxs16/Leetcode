'''
@Author: Xinsheng Guo
@Time: 2020-12-21 14:01:50
@File: 0599_Minimum_Index_Sum_of_Two_Lists.py
@Link: https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/
@Tag: Hash Table
'''
#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#
#%%
# @lc code=start
from collections import defaultdict
class Solution:
    def findRestaurant(self, list1, list2):
        index_dict = defaultdict(list)
        for i, ele in enumerate(list1+list2):
            index_dict[ele].append(i)
        sum_list = [sum(i) for i in index_dict.values() if len(i) == 2]
        minimum = min(sum_list)
        result = []
        for i, j in index_dict.items():
            if sum(j) == minimum and len(j) > 1:
                result.append(i)
        return result
# @lc code=end
#%%
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Solution().findRestaurant(list1, list2)
# %%
