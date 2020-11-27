'''
@Author: Xinsheng Guo
@Time: 2020-11-21 16:45:14
@File: 0028_Implement_strStr().py
@Link: https://leetcode-cn.com/problems/implement-strstr/
@Tag: Two Pointers; String
'''
#%%
class Solution:
    def get_next(self, needle: str, length: int) -> list:
        next_dict = {}
        point = next_dict[0] = -1
        index = 0
        while index < length-1:
            if needle[index] == needle[point] or point < 0:
                point += 1
                index += 1
                next_dict[index] = point
            else:
                point = next_dict[point]
        return next_dict

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        i = 0
        j = 0
        m = len(haystack)
        n = len(needle)
        next_dict = self.get_next(needle, n)
        while j < m and i < n:
            if haystack[j] == needle[i] or i < 0:
                j += 1
                i += 1
            else:
                i = next_dict[i]
        if i == n:
            return j - i
        else:
            return -1
