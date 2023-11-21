class Solution0647 {
    public int countSubstrings(String s) {
        boolean[][] dp = new boolean[s.length()][s.length() + 1];
        int count = s.length();
        for (int i = 0; i < s.length(); i++) {
            dp[i][i + 1] = true;
        }
        for (int i = 0; i < s.length() - 1; i++) {
            int j = i + 2;
            if (s.charAt(i) == s.charAt(j - 1)) {
                dp[i][j] = true;
                count += 1;
            }
        }
        for (int k = 3; k <= s.length(); k++) {
            for (int i = 0; i < s.length(); i++) {
                int j = i + k;
                if (j <= s.length() && s.charAt(i) == s.charAt(j - 1) && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    count += 1;
                }
            }
        }
        return count;
    }
}