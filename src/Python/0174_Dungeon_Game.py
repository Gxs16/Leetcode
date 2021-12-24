class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        row_num = len(dungeon)
        column_num = len(dungeon[0])
        dp = [[1]*column_num for i in range(row_num)]
        if dungeon[-1][-1] < 0:
            dp[-1][-1] = -dungeon[-1][-1]+1
        for j in range(column_num-2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j+1]-dungeon[-1][j])

        for i in range(row_num-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1]-dungeon[i][-1])

        for i in range(row_num-2, -1, -1):
            for j in range(column_num-2, -1, -1):
                dp[i][j] = min(max(1, dp[i][j+1]-dungeon[i][j]), max(1, dp[i+1][j]-dungeon[i][j]))
        return dp[0][0]
