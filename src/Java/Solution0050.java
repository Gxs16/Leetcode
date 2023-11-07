public class Solution0050 {
//    public double myPow(double x, int n) {
//        if (n < 0) {
//            return myPow(1/x, -n);
//        }
//        double[] record = new double[34];
//        record[0] = x;
//        int factor = 1;
//        double res = 1;
//        int mi = 0;
//        while (n > 0) {
//            factor *= 2;
//            mi += 1;
//            if (record[mi] == 0) {
//                record[mi] = record[mi-1] * record[mi-1];
//            }
//            if (factor > n) {
//                res *= record[mi-1];
//                n -= (factor/2);
//                factor=1;
//                mi = 0;
//            }
//        }
//        return res;
//    }
    public double myPow(double x, int n) {
        if (n == Integer.MIN_VALUE) {
            double res = myPow(x, n/2);
            return res * res;
        }
        if (n < 0) {
            return myPow(1/x, -n);
        }
        if (n == 0 || x == 1) {
            return 1;
        }
        if (n % 2 == 0) {
            double res = myPow(x, n/2);
            return res * res;
        } else {
            double res = myPow(x, (n-1)/2);
            return res * res * x;
        }
    }

    public static void main(String[] args) {
        Solution0050 solution = new Solution0050();
        System.out.println(solution.myPow(1.00000, -2147483648));
//        System.out.println(Math.pow(0.00001, 2147483647));
    }
}
