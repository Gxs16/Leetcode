'''
@Author: Xinsheng Guo
@Time: 2020-11-25 22:27:55
@File: 0485_Max_Consecutive_Ones.py
@Link: https://leetcode-cn.com/problems/max-consecutive-ones/
@Tag: Array; Sort
'''
#%%
class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        index = 0
        start = 0
        length_max = 0
        while index < len(nums):
            if nums[index] == 0:
                if start != -1:
                    _length = index-start
                    if _length > length_max:
                        length_max = _length
                    start = -1
                index += 1
            elif nums[index] == 1:
                if start == -1:
                    start = index
                index += 1
        if start != -1:
            _length = index-start
            if _length > length_max:
                return _length
        return length_max
#%%
a = [0,0,0,0]
Solution().findMaxConsecutiveOnes(a)
# %%
