import java.util.LinkedList;
import java.util.List;

public class Solution0047 {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new LinkedList<>();
        boolean[] indexSelected = new boolean[nums.length];
        LinkedList<Integer> comb = new LinkedList<>();
        dfs(res, indexSelected, comb, nums);
        return res;
    }

    public void dfs(List<List<Integer>> res, boolean[] indexSelected, LinkedList<Integer> comb, int[] nums) {
        if (comb.size() == nums.length) {
            res.add(new LinkedList<>(comb));
            return;
        }
        int numSelected = 0;
        for (int i = 0; i < nums.length; i++) {
            if ((!indexSelected[i]) && ((numSelected | (1 << (nums[i] + 10))) != numSelected)) {
                indexSelected[i] = true;
                numSelected = numSelected | (1 << (nums[i] + 10));
                comb.add(nums[i]);
                dfs(res, indexSelected, comb, nums);
                comb.pollLast();
                indexSelected[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        Solution0047 solution = new Solution0047();
        System.out.println(solution.permuteUnique(new int[]{1, 1, 2}));
    }
}
