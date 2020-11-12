'''
@Author: Xinsheng Guo
@Time: 2020-11-12 22:26
@File: 0035_Search_Insert_Position.py
@Link: https://leetcode-cn.com/problems/search-insert-position/
@Tag: Array; Binary Search
'''
class Solution:
    def getPosition(self, nums, target, left, right):
        if left == right:
            if target > nums[right]:
                return right+1
            else:
                return left
        elif right == left+1:
            if target <= nums[left]:
                return left
            elif target > nums[right]:
                return right+1
            else:
                return right
        else:
            position = (left+right)//2
            if nums[position] < target:
                left = position+1
                return self.getPosition(nums, target, left, right)
            elif nums[position] > target:
                right = position-1
                return self.getPosition(nums, target, left, right)
            else:
                return position

    def searchInsert(self, nums, target: int) -> int:
        left = 0
        right = len(nums)-1
        return self.getPosition(nums, target, left, right)

if __name__ == '__main__':
    s = Solution()
    nums = [3]
    target = 3
    print(s.searchInsert(nums, target))
