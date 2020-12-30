'''
@Author: Xinsheng Guo
@Time: 2020 11 22 23:29:13
@File: 0028_Implement_strStr().py
@Link: https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
@Tag: Two Pointers; Array; Binary Search
'''
#%%
class Solution:
    def twoSum(self, numbers, target: int):
        m = len(numbers)
        right = m-1
        for base in range(m):
            left = base+1
            while right >= left:
                index = (right+left)//2
                if numbers[base]+numbers[index] > target:
                    right = index-1
                elif numbers[base]+numbers[index] < target:
                    left = index+1
                else:
                    return [base+1, index+1]
