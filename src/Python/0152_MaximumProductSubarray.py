class Solution:
    def maxProduct(self, nums) -> int:
        max_res = [1]*len(nums)
        min_res = [1]*len(nums)
        for i in range(len(nums)):
            num = nums[i]
            if num >= 0:
                max_res[i] = max(num, max_res[i-1]*num)
                min_res[i] = min(num, min_res[i-1]*num)
            else:
                max_res[i] = max(num, min_res[i-1]*num)
                min_res[i] = min(num, max_res[i-1]*num)
        return max(max_res)