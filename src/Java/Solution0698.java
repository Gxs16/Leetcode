import java.util.Arrays;

class Solution0698 {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = Arrays.stream(nums).sum();
        int target = 0;
        if (sum % k != 0) {
            return false;
        } else {
            target = sum / k;
        }
        // System.out.println(target);
        // System.out.println("===");
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        boolean[] selected = new boolean[nums.length];
        for (int i = nums.length - 1; i >= 0; i--) {
            if (selected[i]) {
                continue;
            }
            if (dfs(nums, selected, target - nums[i], i)) {
                System.out.println(i);
                selected[i] = true;
            } else {
                return false;
            }
        }
        return true;
    }

    public boolean dfs(int[] nums, boolean[] selected, int target, int start) {
        // System.out.println(target);
        if (target == 0) {
            return true;
        } else if (target < 0) {
            return false;
        } else {
            for (int i = start - 1; i >= 0; i--) {
                if (!selected[i]) {
                    if (dfs(nums, selected, target - nums[i], i)) {
                        System.out.println(i);
                        selected[i] = true;
                        return true;
                    }
                }
            }
            return false;
        }

    }

    public static void main(String[] args) {
        System.out.println(1 >> 1);
    }
}
