class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        dp = [[i] for i in nums]
        max_result = [nums[0]]
        max_length = 1
        for i in range(len(nums)):
            result = 0
            tmp = dp[i]
            for j in range(0, i):
                if nums[i]%nums[j] == 0:
                    if len(dp[j])+1 > result:
                        dp[i] = dp[j]+tmp
                        result = len(dp[i])
                if result > max_length:
                    max_length = result
                    max_result = dp[i]
        return max_result

if __name__ == '__main__':
    print(Solution().largestDivisibleSubset([1,2,4,8]))
#%%
print([i for i in range(5,0,-1)])
# %%
