class Solution {
    public int maximumSwap(int num) {
        int [] digits = new int[8];
        int i = 0;
        while (num > 0) {
            digits[i] = num % 10;
            num = num/10;
            i ++;
        }
        
        int flag = 999;
        for (int j = i-1; j >= 0; j --) {
            int maxDigit = 0;
            if (flag < j && digits[flag] > digits[j]) {
                int a = digits[flag];
                digits[flag] = digits[j];
                digits[j] = a;
                break;
            }
            for (int k = j-1; k >= 0; k--) {
                if (maxDigit <= digits[k]) {
                    maxDigit = digits[k];
                    flag = k;
                }
            }
            if (maxDigit > digits[j]) {
                digits[flag] = digits[j];
                digits[j] = maxDigit;
                break;
            }
            
        }
        int res = 0;
        for (int l = 0; l < i; l ++) {
            res += digits[l]*(int)Math.pow(10, l);
        }
        return res;
    }
}