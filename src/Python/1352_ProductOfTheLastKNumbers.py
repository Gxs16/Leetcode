class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        prod = [1]*(len(nums)+1)
        left = 0
        for i in range(len(nums)):
            prod[i+1] = prod[i]*nums[i]
            if nums[i] <= k:
                while prod[i+1]/prod[left] >= k and left <= i:
                    left += 1
                result += i+1-left
            else:
                left = i+1
        return result