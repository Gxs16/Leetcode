'''
@Author: Xinsheng Guo
@Time: 2020-11-18 23:52:11
@File: 0334_Reverse_String.py
@Link: https://leetcode-cn.com/problems/reverse-string/
@Tag: Array
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r=0,len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1

class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]