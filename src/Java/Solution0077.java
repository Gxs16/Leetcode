import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class Solution0077 {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new LinkedList<>();

        for (int i = 1; i <= n - k + 1; i++) {
            List<Integer> current = new ArrayList<>(k);
            current.add(i);
            dfs(res, k, current, n);
        }
        return res;
    }

    public void dfs(List<List<Integer>> res, int k, List<Integer> current, int n) {
        if (current.size() == k) {
            res.add(new ArrayList<>(current));
        } else {
            for (int i = current.get(current.size() - 1) + 1; i <= n - k + current.size(); i++) {
                if (!current.contains(i)) {
                    current.add(i);
                    dfs(res, k, current, n);
                    current.remove(current.size() - 1);
                }
            }
        }
    }
}