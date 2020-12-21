'''
@Author: Xinsheng Guo
@Time: 2020年12月21日16:10:00
@File: 0049_Group_Anagrams.py
@Link: https://leetcode-cn.com/problems/group-anagrams/
@Tag: Hash Table; String
'''
#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
#%%
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        result_dict = defaultdict(list)
        for ele in strs:
            _ele_tuple = tuple(sorted(ele))
            result_dict[_ele_tuple].append(ele)
        return list(result_dict.values())
# @lc code=end

#%%
a = ["eat","tea","tan","ate","nat","bat"]
Solution().groupAnagrams(a)
# %%
(1,2,3) is (3,2,1)
# %%
sorted('awsad')
# %%
