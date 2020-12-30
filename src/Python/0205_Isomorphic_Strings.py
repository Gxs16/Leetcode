'''
@Author: Xinsheng Guo
@Time: 2020-12-20 22:02:43
@File: 0205_Isomorphic_Strings.py
@Link: https://leetcode-cn.com/problems/isomorphic-strings/
@Tag: Hash Table
'''
#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
#%%
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphic = dict()
        for i, j in zip(s, t):
            if i in isomorphic.keys():
                if isomorphic[i] != j:
                    return False
            else:
                if j in isomorphic.values():
                    return False
                else:
                    isomorphic[i] = j
        return True
# @lc code=end

#%%
a = {1:2, 3:4}
a.keys
# %%
Solution().isIsomorphic('ab', 'aa')
# %%
