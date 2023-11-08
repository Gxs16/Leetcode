import java.util.Arrays;

public class Solution0031 {
    public void nextPermutation(int[] nums) {
        int i;
        for (i = nums.length - 1; i > 0; i--) {
            if (nums[i - 1] < nums[i]) {
                break;
            }
        }
        if (i > 0) {
            int secondIndex = i;
            for (int k = i - 1; k < nums.length; k++) {
                if (nums[k] <= nums[i - 1]) {
                    continue;
                }
                if (nums[k] < nums[secondIndex]) {
                    secondIndex = k;
                }
            }
            int tmp = nums[i - 1];
            nums[i - 1] = nums[secondIndex];
            nums[secondIndex] = tmp;
        }
        Arrays.sort(nums, i, nums.length);
    }

    public static void main(String[] args) {
        Solution0031 solution = new Solution0031();
//        int[] nums = new int []{1,2,3};
//        int[] nums = new int []{1,2,3};
//        int[] nums = new int []{1};
//        int[] nums = new int []{1,3,2,5,6,2,5,3,4,7,7,2,1};
        int[] nums = new int[]{2, 2, 7, 5, 4, 3, 2, 2, 1};
        solution.nextPermutation(nums);
        System.out.println(Arrays.toString(nums));
    }
}
