import java.util.LinkedList;
import java.util.List;

class Solution0057 {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        boolean inserted = false;
        List<int[]> res = new LinkedList<>();
        for (int[] interval : intervals) {
            if (interval[1] < newInterval[0]) {
                res.add(interval);
            } else if (interval[0] < newInterval[0]
                    && interval[1] <= newInterval[1]) {
                newInterval[0] = interval[0];
            } else if (interval[0] > newInterval[0]
                    && interval[0] <= newInterval[1]
                    && interval[1] > newInterval[1]) {
                newInterval[1] = interval[1];
            } else if (interval[0] > newInterval[1]) {
                if (!inserted) res.add(newInterval);
                inserted = true;
                res.add(interval);
            } else if (interval[0] <= newInterval[0]
                    && interval[1] >= newInterval[1]) {
                inserted = true;
                res.add(interval);
            }

        }
        if (!inserted) res.add(newInterval);
        int[][] ans = new int[res.size()][2];
        for (int i = 0; i < res.size(); ++i) {
            ans[i] = res.get(i);
        }
        return ans;
    }
}