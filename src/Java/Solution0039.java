import java.util.LinkedList;
import java.util.List;

public class Solution0039 {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new LinkedList<>();
        LinkedList<Integer> path = new LinkedList<>();
        dfs(0, path, res, candidates, target, 0);
        return res;
    }

    public void dfs(int sum, LinkedList<Integer> path, List<List<Integer>> res, int[] candidates, int target, int start) {
        if (sum == target) {
            res.add(new LinkedList<>(path));
        } else if (sum < target) {
            for (int j = start; j < candidates.length; j++) {
                int i = candidates[j];
                if (sum + i <= target) {
                    sum += i;
                    path.add(i);
                    dfs(sum, path, res, candidates, target, j);
                    sum -= i;
                    path.pollLast();
                }
            }
        }
    }
}
