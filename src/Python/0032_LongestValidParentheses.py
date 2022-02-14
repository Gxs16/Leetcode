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
            
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s:
            dp = [0]*len(s)
            for i in range(1, len(s)):
                char = s[i]
                if char == ')':
                    j = dp[i-1]
                    if i-1-j >= 0 and s[i-1-j] == '(':
                        dp[i] = 2+dp[i-1]+dp[i-2-j]
            return max(dp)
        else:
            return 0
