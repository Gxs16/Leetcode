class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [i for i in costs]
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
                min_add = 10**9
                for k in range(len(costs[0])):
                    if k != j:
                        min_add = min(min_add, dp[i-1][k])
                dp[i][j] += min_add
        return min(dp[len(costs)-1])
