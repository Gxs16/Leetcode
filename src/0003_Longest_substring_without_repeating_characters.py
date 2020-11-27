'''
@Author: Xinsheng Guo
@Time: 2020-10-22 15:38
@File: 0003_Add_Two_Numbers.py
@Link: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
'''


# def lengthOfLongestSubstring(s: str) -> int:
#     index = [i for i in range(len(s))]
#     for i in range(1, len(s)):
#         index_temp = []
#         for j in index:
#             try:
#                 if s[j+i] not in s[j: j+i]:
#                     index_temp.append(j)
#             except:
#                 pass
#         if len(index_temp) == 0:
#             return i
#         index = index_temp
#     return len(s)

# print(lengthOfLongestSubstring('1111'))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = set()
        n = len(s)
        for i in range(n):
            for j in range(n):
                if s[j] in 
