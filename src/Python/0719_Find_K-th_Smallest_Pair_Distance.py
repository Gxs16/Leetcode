'''
@Author: Xinsheng Guo
@Time: 2021年1月13日17:38:46
@File: 0719_Find_K-th_Smallest_Pair_Distance.py
@Link: https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance/
@Tag: Heap; Array; Binary Search; Two Pointers
'''
#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 k 小的距离对
#
#%%
# @lc code=start
class Solution:
    def find_target(self, nums, target):
        left = 0
        count = 0
        for right, j in enumerate(nums):
            while j-nums[left] > target:
                left += 1
            count += right-left
        return count

    def smallestDistancePair(self, nums, k: int) -> int:
        nums.sort()
        target_max = nums[-1] - nums[0]
        target_min = 0
        while target_max > target_min:
            target = target_min+(target_max-target_min)//2
            if self.find_target(nums, target) >= k:
                target_max = target
            else:
                target_min = target+1
        return target_min
# @lc code=end
#%%
nums = [9,10,7,10,6,1,5,4,9,8]
nums.sort()
Solution().find_target(nums, 2)
# %%
Solution().smallestDistancePair([9,10,7,10,6,1,5,4,9,8],18)
# %%
nums.sort()
nums
# %%
