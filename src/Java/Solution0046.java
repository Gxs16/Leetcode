import java.util.*;

class Solution0046 {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new LinkedList<>();
        int selected = 0;
        int[] combine = new int[nums.length];
        int flag = 0;
        dfs(res, selected, nums, combine, flag);
        return res;
    }

    public void dfs(List<List<Integer>> res, int selected, int[] nums, int[] combine, int flag) {
        if (selected == ((1 << nums.length) - 1)) {
            res.add(Arrays.asList(Arrays.stream(combine).boxed().toArray(Integer[]::new)));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if ((selected | 1 << i) != selected) {
                combine[flag] = nums[i];
                flag += 1;
                selected = selected | 1 << i;
                dfs(res, selected, nums, combine, flag);
                flag -= 1;
                selected = selected ^ (1 << i);
            }
        }
    }

    public static void main(String[] args) {
        Solution0046 solution = new Solution0046();
        System.out.println(solution.permute(new int[]{1, 2, 3}));
    }
}