class Solution0027 {
    public int removeElement(int[] nums, int val) {
        int left = 0;
        for (int right=0; right < nums.length; right++){
            if (nums[right] == val){
                continue;
            }else{
                nums[left] = nums[right];
                left ++;
            }
        }
        return left;
    }
}