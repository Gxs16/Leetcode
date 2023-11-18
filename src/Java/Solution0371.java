public class Solution0371 {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }

    public static void main(String[] args) {
        Solution0371 solution = new Solution0371();
        solution.getSum(1,1);
    }
}
