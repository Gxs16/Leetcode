class Solution {
    public int[] constructArray(int n, int k) {
        int [] res = new int[n];
        for (int i = k+1; i < n; i++) {
            res[i] = i+1;
        }
        for (int i = 0; i < (k+1)/2; i++) {
            res[i*2+1] = k-i+1;
        }
        for (int i = 0; i < k/2+1; i++) {
            res[i*2] = i+1;
        }
        return res;
    }
}