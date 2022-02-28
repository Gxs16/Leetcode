class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        pre_multi = 1
        post_multi = 1
        for i in range(len(nums)-1):
            pre_multi *= nums[i]
            result[i+1] *= pre_multi
            post_multi *= nums[-1-i]
            result[-2-i] *= post_multi
        return result
