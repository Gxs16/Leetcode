import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

class Solution0040 {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> res = new LinkedList<>();
        LinkedList<Integer> path = new LinkedList<>();
        dfs(0, path, res, candidates, target, -1);
        return res;
    }
    public void dfs(int sum, LinkedList<Integer> path, List<List<Integer>> res, int[] candidates, int target, int start) {
        if (sum == target) {
            res.add(new LinkedList<>(path));
        } else if (sum < target) {
            for (int j = start+1; j < candidates.length; j++) {
                if (j > start+1 && candidates[j]==candidates[j-1]) continue;
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

    public static void main(String[] args) {
        Solution0040 solution = new Solution0040();
        System.out.println(solution.combinationSum2(new int[] {2,5,2,1,2}, 5));
    }
}