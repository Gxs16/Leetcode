class Solution {
    public int searchInsert(int[] nums, int target) {
        int right = nums.length;
        int left = -1;
        while (right > left+1){
            int mid = (right+left)/2;
            if (nums[mid]==target){
                return mid;
            }else{
                if (nums[mid]<target){
                    left = mid;
                }else{
                    right = mid;
                }
            }
        }
        return right;
    }
}