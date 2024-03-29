import java.util.Arrays;

class Solution1608 {
    public int specialArray(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= nums.length - i) {
                if (i > 0) {
                    if (nums[i - 1] < nums.length - i) {
                        return nums.length - i;
                    }
                } else {
                    return nums.length - i;
                }
            }
        }
        return -1;
    }
}