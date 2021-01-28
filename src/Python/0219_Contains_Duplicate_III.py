'''
@Author: Xinsheng Guo
@Time: 2021年1月28日16:44:02
@File: 0219_Contains_Duplicate_III.py
@Link: https://leetcode-cn.com/problems/contains-duplicate-iii/
@Tag: Hash Map
'''
#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
#%%
# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        all_buckets = {}
        bucket_size = t + 1 # 这里将桶的大小定义为t+1是因为这样才能满足桶内包含的数字的差值的绝对值<=t
        for i in range(len(nums)):
            ndx = nums[i] // bucket_size # 计算桶的下标
            if ndx in all_buckets: # 这个位置的桶已经存在了（已经被放进去元素了）
                return True
            else:
                all_buckets[ndx] = nums[i] # 放入桶中
            if (ndx - 1) in all_buckets and abs(all_buckets[ndx-1] - nums[i]) <= t: # 检查前一个桶
                return True
            if (ndx + 1) in all_buckets and abs(all_buckets[ndx+1] - nums[i]) <= t: # 检查后一个桶
                return True
            if i >= k: # 删除下标超出k范围的桶中的元素
                all_buckets.pop(nums[i-k] // bucket_size)
        return False
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums, k, t):
#         """
#         :type nums: List[int]
#         :type k: int
#         :type t: int
#         :rtype: bool
#         """

#         n = len(nums)
#         if n <= 1:
#             return False

#         recode = set()

#         for i in range(n):
#             for one in recode:
#                 if abs(nums[i] - one) <= t:
#                     return True
#             recode.add(nums[i])

#             if (len(recode) > k):
#                 recode.remove(nums[i - k])

#         return False

# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
#         for i in range(len(nums)):
#             if t == 0:
#                 if nums[i] in set(nums[i+1: min(i+k+1, len(nums))]):
#                     return True
#             else:
#                 if nums[i] in set(nums[i+1: min(i+k+1, len(nums))]):
#                     return True
#                 for j in nums[i+1: min(i+k+1, len(nums))]:
#                     if (abs(nums[i]-j) <= t):
#                         return True
#         return False
# @lc code=end
#%%
Solution().containsNearbyAlmostDuplicate([1,2,3,1],3,0)
