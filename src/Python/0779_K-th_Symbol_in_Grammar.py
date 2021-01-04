'''
@Author: Xinsheng Guo
@Time: 2021年1月4日17:48:19
@File: 0779_K-th_Symbol_in_Grammar.py
@Link: https://leetcode-cn.com/problems/k-th-symbol-in-grammar/
@Tag: Recursion
'''
#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#
#%%
# @lc code=start
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        else:
            return (1 - K%2) ^ self.kthGrammar(N-1, (K+1)//2)
# @lc code=end
#%%
Solution().kthGrammar(3, 2)

# %%
0**0
# %%
