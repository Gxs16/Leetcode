class Solution0075 {
    public void sortColors(int[] nums) {
        int left = -1;
        int right = nums.length;
        for (int i = 0; i < nums.length; i ++) {
            if (nums[i] == 0) {
                left += 1;
            } else if (nums[i] == 2) {
                right -= 1;
            }
        }
        for (int i = 0; i <= left; i ++) {
            nums[i] = 0;
        }
        for (int i = left + 1; i < right; i++) {
            nums[i] = 1;
        }
        for (int i = right; i < nums.length; i++) {
            nums[i] = 2;
        }
    }
}