'''
@Author: Xinsheng Guo
@Time: 2020-11-11 23:15
@File: 0724_Find_Pivot_index.py
@Link: https://leetcode-cn.com/problems/find-pivot-index/
@Tag: Array
'''

class Solution:
    def pivotIndex(self, nums) -> int:
        if nums:
            sum1 = 0
            sum2 = sum(nums[1:])
            for i in range(len(nums)):
                if sum1 == sum2:
                    return i
                else:
                    sum1 += nums[i]
                    if i+1 < len(nums):
                        sum2 -= nums[i+1]
            return -1
        else:
            return -1

class Solution2:
    def pivotIndex(self, nums) -> int:
        if nums:
            for i in range(0, len(nums)):
                if sum(nums[:i]) == sum(nums[i+1:]):
                    return i
            return -1
        else:
            return -1
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    print(s.pivotIndex(nums))
    for i in range(len(nums)):
        print(i)