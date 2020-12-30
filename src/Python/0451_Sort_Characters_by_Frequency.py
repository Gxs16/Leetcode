'''
@Author: Xinsheng Guo
@Time: 2020年12月22日16:13:55
@File: 0451_Sort_Characters_by_Frequency.py
@Link: https://leetcode-cn.com/problems/sort-characters-by-frequency/
@Tag: Heap; Hash Table
'''
#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#
#%%
# @lc code=start
from collections import Counter, defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        relation = defaultdict(list)
        result = ''
        for i, j in count.items():
            relation[j].append(i)
        for i in sorted(relation, reverse=True):
            for k in relation[i]:
                result += k*i
        return result
        
# @lc code=end
#%%
Solution().frequencySort('raaeaedere')
#%%
count = Counter('raaeaedere')
# %%
count
# %%
a = [1,2,3,4]
a.sort(reverse=True)
a
# %%
