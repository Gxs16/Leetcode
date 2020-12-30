'''
@Author: Xinsheng Guo
@Time: 2020-12-18 17:33:51
@File: 0136_Single_Number.py
@Link: https://leetcode-cn.com/problems/single-number/
@Tag: Hash Table; Bit Manipulation
'''
#%%
class Solution:
    def singleNumber(self, nums) -> int:
        nums_all = set(nums)
        nums_set = set()
        for i in nums:
            if i in nums_set:
                nums_all -= {i}
            else:
                nums_set.add(i)
        for i in nums_all:
            return i
# %%
Solution().singleNumber([1,2,3,2,1])
# %%
