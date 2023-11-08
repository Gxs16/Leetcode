import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution0015 {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
//                i++;
                continue;
            }
            int left = i + 1;
            int right = nums.length - 1;
            boolean hasOne = false;
            while (left < right) {
                if (nums[i] + nums[left] + nums[right] == 0) {
                    if (hasOne && nums[left] == nums[left - 1]) {
                        left += 1;
                        continue;
                    }
                    hasOne = true;
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left += 1;
                    right -= 1;
                } else if (nums[i] + nums[left] + nums[right] > 0) {
                    right -= 1;
                } else {
                    left += 1;
                }
            }
        }
        return res;
    }
}

