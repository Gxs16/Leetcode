'''
@Author: Xinsheng Guo
@Time: 2021年12月1日
@File: 0042_Trapping_Rain_Water.py
@Link: https://leetcode-cn.com/problems/trapping-rain-water/
'''
#%%
class Solution:
    def trap(self, height: list) -> int:
        total_rain = 0
        left = 0
        right = len(height)-1
        while left < right:
            if height[left+1] >= height[left]:
                left += 1
                continue
            if height[right-1] >= height[right]:
                right -= 1
                continue
            height_sum = 0

            height_left = height[left]
            middle = left+1
            while middle <= right:
                if height[middle] <= height_left:
                    height_sum += (height_left-height[middle])
                    middle += 1
                else:
                    total_rain += height_sum
                    left = middle
                    break
            height_sum = 0

            height_right = height[right]
            middle = right-1
            while middle >= left:
                if height[middle] < height_right:
                    height_sum += (height_right-height[middle])
                    middle -= 1
                else:
                    total_rain += height_sum
                    right = middle
                    break
        return total_rain
#%%
Solution().trap([4,2,3])