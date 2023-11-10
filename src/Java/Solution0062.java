public class Solution0062 {
    public int uniquePaths(int m, int n) {
        if (m == 1 && n == 1) return 1;
        double big = m+n-2;
        double one = 1;
        double two = 1;
        for (int i = 0; i < Math.min(m,n)-1; i++) {
            one *=  (big - i);
        }
        for (int i = 1; i <= Math.min(m,n)-1; i ++) {
            two *= i;
        }
//        System.out.println(one);
        return (int) (one/two);
    }

    public static void main(String[] args) {
        Solution0062 solution = new Solution0062();
        int res = solution.uniquePaths(10, 10);
        System.out.println(res);
    }
}
