'''
@Author: Xinsheng Guo
@Time: 2020-12-10 14:54:26
@File: 0020_Valid_Parentheses.py
@Link: https://leetcode-cn.com/problems/valid-parentheses/
@Tag: Linked List; Two Pointers
'''
#%%
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pair = {')':'(', '}':'{', ']':'['}
        parent_stack = []
        for i in s:
            if i in pair.values():
                parent_stack.append(i)
            else:
                if parent_stack:
                    if parent_stack[-1] == pair[i]:
                        parent_stack.pop()
                    else:
                        return False
                else:
                    return False
        if parent_stack:
            return False
        else:
            return True
#%%
Solution().isValid('()')
# %%
