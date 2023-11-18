import java.util.*;

class Solution0090 {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        HashSet<String> records = new HashSet<>();
        List<List<Integer>> res = new ArrayList<>(1 << nums.length);
        for (int i = 0; i < (1 << (nums.length)); i++) {
            List<Integer> subset = new LinkedList<>();
            boolean need = true;
            for (int j = 0; j < nums.length; j++) {
                if ((i & (1 << j)) != 0) {
                    if (j > 0 && (i >> (j - 1) & 1) == 0 && nums[j] == nums[j - 1]) {
                        need = false;
                        break;
                    }
                    int num = nums[j];
                    // pattern.append(num);
                    subset.add(nums[j]);
                }
            }

            if (need) {
                res.add(subset);
            }
        }
        return res;
    }


}