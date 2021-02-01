'''
@Author: Xinsheng Guo
@Time: 2021年2月1日15:58:02
@File: 0394_Decode_String.py
@Link: https://leetcode-cn.com/problems/decode-string/
@Tag: Stack; Depth First Search
'''
#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
#%%
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ']':
                _str = ''
                while stack[-1] != '[':
                    _str = stack.pop()+_str
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                stack.append(int(num)*_str)
            else:
                stack.append(i)
        return ''.join(stack)

# @lc code=end
#%%
Solution().decodeString("3[a2[c]]")
