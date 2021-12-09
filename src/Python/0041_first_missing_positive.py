'''
@Author: Xinsheng Guo
@Time: 2021年12月9日
@File: 0041_first_missing_positive.py
@Link: https://leetcode-cn.com/problems/first-missing-positive/
'''

#%%
class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1

        for i in nums:
            if abs(i) <= n:
                nums[abs(i)-1] = -abs(nums[abs(i)-1])

        for i in range(n):
            if nums[i] > 0:
                return i+1

        return n+1

#%%
b = {0,1,2,3,4,5,6,7,8,9}
for i in range(100000000):
    10 in b
# %%
a = {0:0,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
for i in range(100000000):
    5 in a
# %%
