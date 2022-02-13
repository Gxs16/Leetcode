class Solution:
    def lenLongestFibSubseq(self, arr) -> int:
        dp = [[2]*len(arr) for i in arr[0:-1]]
        result = 0
        for i in range(2, len(arr)):
            k = i-1
            j = 0
            while j < k:
                if arr[k]+arr[j] == arr[i]:
                    dp[k][i] = dp[j][k] + 1
                    result = max(result, dp[k][i])
                    k -= 1
                    j += 1
                elif arr[k]+arr[j] > arr[i]:
                    k -= 1
                else:
                    j += 1

        return result
