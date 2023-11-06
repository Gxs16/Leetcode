import java.util.Arrays;

class Solution1619 {
    public double trimMean(int[] arr) {
        Arrays.sort(arr);
        int len = (int) (0.05 * arr.length);
        int total = arr.length - len;
        double sum = 0.0;
        for (int i = len; i < total; i++) {
            sum += arr[i];
        }
        return sum / (total - len);
    }
}