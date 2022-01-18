class Solution:
    def maxSumOfThreeSubarrays(self, nums, k: int):
        dp = [0, [0, k], [0, k, 2*k]]
        sum_dict = {}
        sum_dict[0] = sum(nums[0:k])
        for i in range(1, len(nums)-k+1):
            sum_dict[i] = sum_dict[i-1]-nums[i-1]+nums[i+k-1]
        sums = [sum_dict[0], sum_dict[k]+sum_dict[0], sum_dict[2*k]+sum_dict[k]+sum_dict[0]]
        for idx2 in range(2*k+1, len(nums)-k+1):
            idx1 = idx2-k
            idx0 = idx1-k
            if sum_dict[idx0] > sums[0]:
                dp[0] = idx0
                sums[0] = sum_dict[idx0]
            if sum_dict[idx1]+sums[0] > sums[1]:
                dp[1] = [dp[0], idx1]
                sums[1] = sum_dict[idx1]+sums[0]
            if sum_dict[idx2]+sums[1] > sums[2]:
                dp[2] = dp[1] + [idx2]
                sums[2] = sum_dict[idx2]+sums[1]
        return dp[2]