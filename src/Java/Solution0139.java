import java.util.List;

class Solution0139 {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (String word : wordDict) {
                if (i - word.length() < 0) {
                    continue;
                }
                boolean equals = word.equals(s.substring(i - word.length(), i));
                if (i - word.length() == 0) {
                    dp[i] = equals || dp[i];
                    continue;
                }
                dp[i] = (dp[i - word.length()] && equals) || dp[i];
            }
        }
        return dp[s.length()];
    }
}