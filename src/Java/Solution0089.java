import java.util.ArrayList;
import java.util.List;

class Solution0089 {
    public List<Integer> grayCode(int n) {
        List<Integer> res = new ArrayList<>(1 << n);
        boolean[] numSet = new boolean[1 << n];
        res.add(0);
        numSet[0] = true;
        dfs(res, numSet, n);
        return res;

    }

    public boolean dfs(List<Integer> path, boolean[] numSet, int n) {
        if (path.size() == (1 << n)) {
            return true;
        } else {
            int last = path.get(path.size() - 1);
            for (int i = 0; i < n; i++) {
                int next = last ^ (1 << i);
                if (!numSet[next]) {
                    numSet[next] = true;
                    path.add(next);
                    boolean res = dfs(path, numSet, n);
                    if (res) {
                        return res;
                    } else {
                        path.remove(path.size() - 1);
                        numSet[next] = false;
                    }
                }
            }
            return false;

        }
    }
}