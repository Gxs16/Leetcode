class Solution0055 {
    public boolean canJump(int[] nums) {
        boolean[] dp = new boolean[nums.length];
        dp[nums.length - 1] = true;
        for (int i = nums.length - 1; i >= 0; i--) {
            for (int j = 0; j <= nums[i]; j++) {
                if (i + j < nums.length) {
                    dp[i] = dp[i] || dp[i + j];
                }
                if (dp[i]) {
                    break;
                }
            }
        }
        
        return dp[0];
    }
}
