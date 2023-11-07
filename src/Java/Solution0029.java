public class Solution0029 {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE) {
            if (divisor == 1) {
                return Integer.MIN_VALUE;
            }
            if (divisor == -1) {
                return Integer.MAX_VALUE;
            }
        }
        boolean reverse = false;
        if (dividend > 0) {
            dividend = -dividend;
            reverse = !reverse;
        }
        if (divisor > 0) {
            divisor = -divisor;
            reverse = !reverse;
        }
        if (dividend > divisor) return 0;
        int ans = 1;
        int divisorCopy = divisor;
        while (dividend - divisorCopy <= divisorCopy) {
            ans += ans;
            divisorCopy += divisorCopy;
        }
        if (reverse) {
            return -ans - divide(dividend - divisorCopy, divisor);
        }
        return ans + divide(dividend - divisorCopy, divisor);
    }


    public static void main(String[] args) {
        Solution0029 solution = new Solution0029();
        System.out.println(solution.divide(1100540749, -1090366779));
        System.out.println(1);
    }
}
