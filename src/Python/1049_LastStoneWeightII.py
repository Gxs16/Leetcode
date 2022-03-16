class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        diff = sum(stones)
        dp = [False]*diff+[True]
        for stone in stones:
            for j in range(0,diff-2*stone+1):
                dp[j] = dp[j+2*stone] or dp[j]
        for i in range(diff+1):
            if dp[i]:
                return i
