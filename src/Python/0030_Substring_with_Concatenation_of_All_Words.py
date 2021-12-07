'''
@Author: Xinsheng Guo
@Time: 2021年12月7日
@File: 0030_Substring_with_Concatenation_of_All_Words.py
@Link: https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/
'''
#%%
class Solution:
    def findSubstring(self, s: str, words):
        result = []
        word_dict = {}
        length = len(words[0])
        total_length = len(words)*length
        length_s = len(s)
        if length_s < total_length:
            return result
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

        for i in range(length):
            j = i
            dict_temp = {}
            substring = s[i: i+total_length-length]
            for k in range(0, len(substring), length):
                if substring[k: k+length] in word_dict:
                    if substring[k: k+length] in dict_temp:
                        dict_temp[substring[k: k+length]] += 1
                    else:
                        dict_temp[substring[k: k+length]] = 1
            for j in range(i, length_s-total_length+1, length):
                substring = s[j: j+total_length]
                if substring[-length:] in word_dict:
                    if substring[-length:] in dict_temp:
                        dict_temp[substring[-length:]] += 1
                    else:
                        dict_temp[substring[-length:]] = 1
                if dict_temp == word_dict:
                    result.append(j)
                if substring[0: length] in dict_temp:
                    dict_temp[substring[0: length]] -= 1
                
        return result
                
                

#%%
Solution().findSubstring("dddddddddddd", ["dddd","dddd"])# %%
#%%
a = {1:2}
b = {}
b[1] = 2
a == b
# %%
