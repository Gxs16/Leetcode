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
    def get_dict(self, s: str, index_dict: dict) -> dict:
        if index_dict:
            for i, j in index_dict.items():
                if i-1 < 0 or j+1 >= len(s):
                    pass

    def longestPalindrome(self, s: str) -> str:
        index_dict = {}

