class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum%k != 0:
            return False
        else:
            target = total_sum//k
        if max(nums) > target:
            return False
        nums.sort(reverse=True)
        def dfs(i, j, k, subsets, nums, target):
            if nums[i]+subsets[j] == target:
                subsets[j] += nums[i]
                if i == len(nums)-1:
                    return True
                return dfs(i+1, 0, k, subsets.copy(), nums, target)
            elif nums[i]+subsets[j] < target:
                _subsets = subsets.copy()
                _subsets[j] += nums[i]
                if i == len(nums)-1:
                    return False
                if dfs(i+1, 0, k, _subsets, nums, target):
                    return True
                else:
                    res1 = False
                    res2 = False
                if j < k-1:
                    res2 = dfs(i, j+1, k, subsets.copy(), nums, target)
                return res1 or res2
            else:
                if j == k-1:
                    return False
                return dfs(i, j+1, k, subsets.copy(), nums, target)
        return dfs(0, 0, k, [0]*k, nums, target)