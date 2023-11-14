public class Solution0081 {
    public boolean search(int[] nums, int target) {
        int start = 0;
        int end = nums.length-1;

        if (nums[0] >= nums[nums.length-1]) {
            int numEnd = binarySearch(nums, 0, nums.length-1);
            if (target > nums[0]) {
                end = numEnd;
            } else if (target == nums[0]) {
                return true;
            } else {
                start = numEnd+1;
            }
        }
        while(start <= end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] == target) {
                return true;
            } else if (nums[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return false;
    }

    public int binarySearch(int[] nums, int left, int right) {
        if (left == right-1 && nums[left] <= nums[right]) {
            return -1;
        }
        while (left < right-1) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[left]) {
                left = mid;
            } else if (nums[mid] < nums[right]) {
                right = mid;
            } else if (nums[mid] == nums[left] && nums[mid] > nums[right]) {
                left = mid;
            } else if (nums[mid] == nums[right] && nums[mid] < nums[left]) {
                right = mid;
            } else {
                int end = binarySearch(nums, mid, right);
                if (end != -1) {
                    return end;
                } else {
                    return binarySearch(nums, left, mid);
                }
            }
        }
        return left;
    }

    public static void main(String[] args) {
        Solution0081 solution = new Solution0081();
        System.out.println(solution.search(new int[] {1,0,1,1,1}, 0));
    }
}
