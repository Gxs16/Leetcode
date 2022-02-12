class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) >= 4:
            dp_left = [0] * (len(nums)-1)
            for i in range(len(nums)-1):
                dp_left[i] = max(dp_left[i-2], dp_left[i-3]) + nums[i]
            dp_right = [0] * (len(nums)-1)
            for i in range(len(nums)-1):
                dp_right[i] = max(dp_right[i-2], dp_right[i-3]) + nums[i+1]
            return max(dp_left[-1], dp_left[-2], dp_right[-1], dp_right[-2])
        else:
            return max(nums)