class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [[0]*len(prob) for i in range(target+1)]
        dp[0][0] = 1-prob[0]
        for i in range(1, len(prob)):
            dp[0][i] = dp[0][i-1]*(1-prob[i])
        for i in range(1, target+1):
            result = 1
            for k in range(i):
                result *= prob[k]
            dp[i][i-1] = result
            for j in range(i, len(prob)):
                dp[i][j] = dp[i-1][j-1]*prob[j]+dp[i][j-1]*(1-prob[j])
        return dp[target][-1]
