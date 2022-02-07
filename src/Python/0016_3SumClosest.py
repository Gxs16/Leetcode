class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        diff = 10**9
        for i in range(0, len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                sums = nums[i]+nums[left]+nums[right]
                if sums > target:
                    _diff = sums-target
                    right -= 1
                elif sums < target:
                    _diff = target-sums
                    left += 1
                else:
                    return target
                if _diff < diff:
                    diff = _diff
                    result = sums
        return result
