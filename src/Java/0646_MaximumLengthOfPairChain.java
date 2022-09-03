class Solution {
    public int findLongestChain(int[][] pairs) {
        int curr = -1001, res = 0;
        Arrays.sort(pairs, (a, b) -> a[1] - b[1]);
        for (int[] p : pairs) {
            if (curr < p[0]) {
                curr = p[1];
                res++;
            }
        }
        return res;
    }
}