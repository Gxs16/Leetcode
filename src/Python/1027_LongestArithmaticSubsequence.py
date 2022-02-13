class Solution:
    def longestArithSeqLength(self, nums) -> int:
        dp = {}
        result = 2
        for i in range(1, len(nums)):
            for j in range(0, i):
                d = nums[i]-nums[j]
                dp[(i, d)] = dp.get((j, d), 1)+1
        return max(list(dp.values()))
