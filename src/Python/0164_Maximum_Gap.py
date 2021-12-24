class Solution:
    def maximumGap(self, nums) -> int:
        num_max = max(nums)
        eps = 0.1
        while num_max > eps:
            bucket = [[] for i in range(10)]
            eps *= 10
            for num in nums:
                key = int((num/eps)%10)
                bucket[key].append(num)
            nums = []
            for i in bucket:
                nums.extend(i)
            
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i]-nums[i-1])
        return max_gap