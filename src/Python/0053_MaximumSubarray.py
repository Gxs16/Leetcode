class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_res = -10**9
        cur_res = 0
        for num in nums:
            if num > 0:
                cur_res += num
                max_res = max(max_res, num, cur_res)
            elif num == 0:
                max_res = max(max_res, num)
            else:
                max_res = max(max_res, num)
                if cur_res + num > 0:
                    cur_res += num
                else:
                    cur_res = 0
        return max_res