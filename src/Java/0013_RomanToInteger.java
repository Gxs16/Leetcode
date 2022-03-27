class Solution {
    public int romanToInt(String s) {
        int[] dp = new int[s.length()+1];
        dp[0] = 0;
        for (int i=0; i<s.length(); i++){
            if (s.charAt(i) == 'I'){
                dp[i+1] = dp[i]+1;
            }
            if (s.charAt(i) == 'V'){
                if (i >= 1 && s.charAt(i-1)=='I'){
                    dp[i+1] = dp[i-1]+4;
                }else{
                    dp[i+1] = dp[i]+5;
                }
            }
            if (s.charAt(i) == 'X'){
                if (i >= 1 && s.charAt(i-1)=='I'){
                    dp[i+1] = dp[i-1]+9;
                }else{
                    dp[i+1] = dp[i]+10;
                }
            }
            if (s.charAt(i) == 'L'){
                if (i >= 1 && s.charAt(i-1)=='X'){
                    dp[i+1] = dp[i-1]+40;
                }else{
                    dp[i+1] = dp[i]+50;
                }
            }
            if (s.charAt(i) == 'C'){
                if (i >= 1 && s.charAt(i-1)=='X'){
                    dp[i+1] = dp[i-1]+90;
                }else{
                    dp[i+1] = dp[i]+100;
                }
            }
            if (s.charAt(i) == 'D'){
                if (i >= 1 && s.charAt(i-1)=='C'){
                    dp[i+1] = dp[i-1]+400;
                }else{
                    dp[i+1] = dp[i]+500;
                }
            }
            if (s.charAt(i) == 'M'){
                if (i >= 1 && s.charAt(i-1)=='C'){
                    dp[i+1] = dp[i-1]+900;
                }else{
                    dp[i+1] = dp[i]+1000;
                }
            }
        }
        return dp[s.length()];
    }
    
}