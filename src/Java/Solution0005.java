class Solution0005 {
    public String longestPalindrome(String s) {
        boolean[][] length = new boolean[s.length()][s.length()];

        String res = s.substring(0, 1);
        for (int i = 0; i < s.length(); i++) {
            length[i][i] = true;
        }
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                length[i][i + 1] = true;
                res = s.substring(i, i + 2);
            }
        }
        for (int l = 2; l <= s.length() - 1; l++) {
            for (int i = 0; i < s.length() - l; i++) {
                length[i][i + l] = (s.charAt(i) == s.charAt(i + l)) && length[i + 1][i + l - 1];
                if (length[i][i + l] && l + 1 > res.length()) {
                    res = s.substring(i, i + l + 1);

                }
            }
        }

        return res;
    }

    public static void main(String[] args) {
        Solution0005 solution0005 = new Solution0005();

        System.out.println(solution0005.longestPalindrome("aaaab"));
    }
}
