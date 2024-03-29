import java.util.HashMap;

class Solution0001 {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i=0; i < nums.length; i++){
            if (map.containsKey(target-nums[i])){
                result[0] = i;
                result[1] = map.get(target-nums[i]);
                return result;
            }else{
                map.put(nums[i], i);
            }
        }
        return new int[0];
    }
}