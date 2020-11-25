'''
@Author: Xinsheng Guo
@Time: 2020-11-25 23:04:30
@File: 0209_Minimum_Size_Subarray_Sum.py
@Link: https://leetcode-cn.com/problems/max-consecutive-ones/
@Tag: Array; Sort
'''

#%%
class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        left = 0
        right = 0
        length = 0
        while right <= len(nums):
            if sum(nums[left:right]) < s:
                right += 1
            else:
                _length = right - left
                if length == 0:
                    length = _length
                else:
                    if _length < length:
                        length = _length
                left += 1
        return length
# %%
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 双指针解法
        n = len(nums)
        if sum(nums) < s:
            return 0
        rst = n
        left = 0
        tmp_sum = 0
        for right, value in enumerate(nums):
            tmp_sum += value
            while tmp_sum >= s:
                rst = min(rst, right - left + 1)  # 更新长度
                # 左指针右移
                tmp_sum -= nums[left]
                left += 1
        return rst
# %%
