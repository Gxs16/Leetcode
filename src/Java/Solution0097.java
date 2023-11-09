class Solution0097 {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.isEmpty() && s2.isEmpty()) {
            return s3.isEmpty();
        }
        if (s1.isEmpty()) {
            return s2.equals(s3);
        }
        if (s2.isEmpty()) {
            return s1.equals(s3);
        }
        if (s1.length() + s2.length() != s3.length()) {
            return false;
        }
        boolean[][] dp = new boolean[s1.length()+1][s2.length()+1];
        dp[0][0] = true;
        for (int i = 1; i <= s3.length(); i++) {
            for (int l1 = 0; l1 <= Math.min(i, s1.length()); l1++) {
                int l2 = i-l1;
                if (l2 > s2.length()) {
                    continue;
                }
                if (l1 > 0) {
                    dp[l1][l2] = dp[l1][l2] || (s1.charAt(l1-1) == s3.charAt(i-1) && dp[l1-1][l2]);
                }
                if (l2 > 0) {
                    dp[l1][l2] = dp[l1][l2] || (s2.charAt(l2-1) == s3.charAt(i-1) && dp[l1][l2-1]);
                }

            }
        }
        return dp[s1.length()][s2.length()];
    }
}
