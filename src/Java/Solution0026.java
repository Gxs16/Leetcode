class Solution0026 {
    public int removeDuplicates(int[] nums) {
        int left = 1;
        for (int right=1; right < nums.length; right++){
            if (nums[right] == nums[right-1]){
                continue;
            }else{
                nums[left] = nums[right];
                left ++;
            }
        }
        return left;
    }
}