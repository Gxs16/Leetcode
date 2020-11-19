'''
@Author: Xinsheng Guo
@Time: 2020-11-19 22:32:21
@File: 0014_Longest_Common_Prefix.py
@Link: https://leetcode-cn.com/problems/longest-common-prefix/
@Tag: Array
'''
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''
        else:
            prefix = strs[0]
            a = len(prefix)
            for i in range(1, len(strs)):
                target = strs[i]
                b = len(target)
                for j in range(min(a, b)):
                    if prefix[j] != target[j]:
                        prefix = prefix[0:j]
                        a = j
                        break
                else:
                    if a > b:
                        prefix = target
                        a = b        
            return prefix

class Solution2:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''
        else:
            prefix = strs[0]
            a = len(prefix)
            for target in strs[1:]:
                b = len(target)
                for j in range(min(a, b)):
                    if prefix[j] != target[j]:
                        prefix = prefix[0:j]
                        a = j
                        break
                else:
                    if a > b:
                        prefix = target
                        a = b        
            return prefix
S=Solution()
strs = ["ab", "a"]
print(S.longestCommonPrefix(strs))
#%%
a = [1]
for i in a:
    print(i)
# %%
