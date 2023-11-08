class Solution0091 {
    public int numDecodings(String s) {
        int[] dp = new int[s.length()];
        if (s.charAt(0) == '0') {
            return 0;
        }
        if (s.length() == 1) {
            return 1;
        }
        dp[0] = 1;
        if (s.charAt(1) != '0') {
            dp[1] += dp[0];
        }
        if (s.substring(0, 2).compareTo("26") <= 0) {
            dp[1] += 1;
        }
        for (int i = 2; i < s.length(); i++) {
            if (s.charAt(i) != '0') {
                dp[i] += dp[i - 1];
            }
            if (s.charAt(i - 1) != '0' && s.substring(i - 1, i + 1).compareTo("26") <= 0) {
                dp[i] += dp[i - 2];
            }
        }
        return dp[s.length() - 1];
    }
}

