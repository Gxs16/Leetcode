'''
@Author: Xinsheng Guo
@Time: 2020-11-09 22:16
@File: 0005_Longest_Palindromic_Substring.py
@Link: https://leetcode-cn.com/problems/longest-palindromic-substring/
'''

class Solution:
    '''
    动态规划
    '''
    def get_dict(self, s: str, index_list: list) -> list:
        if index_list:
            for i, j in index_list:
                if i-1 < 0 or j+1 >= len(s):
                    pass
                elif s[i-1] == s[j+1]:
                    index_list.append((i-1, j+1))
            return index_list
        else:
            for i in range(1, len(s)-1):
                if s[i-1] == s[i+1]:
                    index_list.append((i-1, i+1))
            for i in range(1, len(s)):
                if s[i-1] == s[i]:
                    index_list.append((i-1, i))
        if index_list:
            index_list = self.get_dict(s, index_list)
            return index_list
        else:
            return [(0,0)]

    def longestPalindrome(self, s: str) -> str:
        index_list = []
        index_list = self.get_dict(s, index_list)
        lenth = 0
        start = 0
        end = 0
        for i, j in index_list:
            if j-i >= lenth:
                lenth = j-i
                start = i
                end = j
        return s[start: end+1]
