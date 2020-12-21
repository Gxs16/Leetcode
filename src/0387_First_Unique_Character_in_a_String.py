'''
@Author: Xinsheng Guo
@Time: 2020-12-17 16:42:07
@File: 0387_First_Unique_Character_in_a_String.py
@Link: https://leetcode-cn.com/problems/first-unique-character-in-a-string/
@Tag: Array
'''
#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        index_dict = defaultdict(list)
        for i, j in enumerate(s):
            index_dict[j].append(i)
        result = [sum(i) for i in index_dict.values() if len(i) == 1]
        if result:
            return min(result)
        else:
            return -1
# @lc code=end
#%%
min([1,2,3])

# %%
