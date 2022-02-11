class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = [nums[0]]
        for i in nums[1:]:
            if i > d[-1]:
                d.append(i)
            elif i < d[-1]:
                left = 0
                right = len(d)
                while right > left:
                    target = (right+left)//2
                    if d[target] > i:
                        right = target
                    elif d[target] == i:
                        left = target
                        break
                    else:
                        left = target+1
                d[left] = i
        return len(d)