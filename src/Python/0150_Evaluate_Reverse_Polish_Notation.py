'''
@Author: Xinsheng Guo
@Time: 2020-11-19 23:28:26
@File: 0150_Evaluate_Reverse_Polish_Notation.py
@Link: https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
@Tag: Stack
'''
#%%
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack[0]
#%%
Solution().evalRPN(["2","1","+","3","*"])
# %%
