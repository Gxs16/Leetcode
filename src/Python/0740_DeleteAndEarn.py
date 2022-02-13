class Solution:
    def deleteAndEarn(self, nums) -> int:
        from collections import Counter
        hash_table = Counter(nums)
        keys = list(hash_table.keys())
        keys.sort()
        dp = [key*hash_table[key] for key in keys]
        for i in range(len(keys)):
            key = keys[i]
            if keys[i-1] == key-1:
                if i-2 >= 0:
                    dp[i] = dp[i-2]+key*hash_table[key]
                if i-3 >= 0:
                    dp[i] = max(dp[i], dp[i-3]+key*hash_table[key])
            else:
                if i-1 >= 0:
                    dp[i] = dp[i-1]+key*hash_table[key]
                if i-2 >= 0:
                    dp[i] = max(dp[i-2]+key*hash_table[key], dp[i])
        if keys[-1]-1 in hash_table:
            return max(dp[-1], dp[-2])
        else:
            return dp[-1]
