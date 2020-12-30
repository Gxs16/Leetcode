'''
@Author: Xinsheng Guo
@Time: 2020-11-24 22:34:42
@File: 0561_Array_Partition_I.py
@Link: https://leetcode-cn.com/problems/array-partition-i/
@Tag: Array; Sort
'''
#%%
import random

class Solution:
    '''
    单边循环实现快排
    '''
    def quick_sort(self, nums, start, end):
        '''
        自写快排
        '''
        if end > start:
            pivot = random.randint(start, end)
            nums[start], nums[pivot] = nums[pivot], nums[start]
            mark = start
            for i in range(start+1, end+1):
                if nums[i] >= nums[start]:
                    continue
                else:
                    mark += 1
                    nums[mark], nums[i] = nums[i], nums[mark]
            nums[mark], nums[start] = nums[start], nums[mark]
            nums = self.quick_sort(nums, start, mark-1)
            nums = self.quick_sort(nums, mark+1, end)
        return nums


    def arrayPairSum(self, nums) -> int:
        nums = self.quick_sort(nums, 0, len(nums)-1)
        result = 0
        for i in nums[0::2]:
            result += i
        return result
#%%
a = [16,1234,5,123,2346,1,1,46,3]
S = Solution()
S.quick_sort(a, 0, len(a)-1)
# %%
