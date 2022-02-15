class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp_prev = 0
        result = 0
        for i in range(2, len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp_prev += 1
                result += dp_prev
            else:
                dp_prev = 0
        return result