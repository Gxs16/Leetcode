class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        diff = 10**9           
        for i in range(left+1, right):
            sums = nums[left]+nums[right]+nums[i]
            if sums > target:
                _diff = sums-target
            elif sums < target:
                _diff = target-sums
            if _diff < diff:
                diff = _diff
                result = sums
                middle = i

        while left < middle:
            left += 1
            if result < target:

        