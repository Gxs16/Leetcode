class Solution0064 {
    public int minPathSum(int[][] grid) {
        int[][] dp = new int[grid.length][grid[0].length];

        for (int i = 0; i < dp.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                int value = Integer.MAX_VALUE;
                if (i > 0) {
                    value = Math.min(value, dp[i - 1][j]);
                }
                if (j > 0) {
                    value = Math.min(value, dp[i][j - 1]);
                }
                dp[i][j] = value + grid[i][j];
                if (i == 0 && j == 0) {
                    dp[i][j] = grid[0][0];
                }
            }
        }
        return dp[grid.length - 1][grid[0].length - 1];
    }
}
