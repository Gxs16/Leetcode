'''
@Author: Xinsheng Guo
@Time: 2021年12月8日
@File: 0032_Longest_Valid_Parentheses.py
@Link: https://leetcode-cn.com/problems/longest-valid-parentheses/
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, i-stack[-1])
                else:
                    stack.append(i)
        return max_len
            

        

#%%
a = [1]
a.pop()
a.pop()
# %%
