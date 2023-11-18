import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

class Solution0056 {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(x -> x[0]));
        List<int[]> result = new ArrayList<>();
        int i = 0;
        int j;
        while (i < intervals.length) {
            int[] base = intervals[i];
            for (j = i + 1; j < intervals.length; j++) {
                if (intervals[j][0] <= base[1] && intervals[j][1] >= base[1]) {
                    base[1] = intervals[j][1];
                } else if (base[1] > intervals[j][1]) {
                } else {
                    break;
                }
            }
            result.add(base);
            i = j;
        }
        int[][] res = new int[result.size()][2];
        return result.toArray(res);
    }
}
