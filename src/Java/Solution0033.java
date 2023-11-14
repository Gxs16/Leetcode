public class Solution0033 {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        int left = 0;
        int right = nums.length - 1;
        if (nums[left] > nums[right]) {
            while (left < right-1) {
                int k = left + (right - left) / 2;
                if (nums[k] > nums[left]) {
                    left = k;
                } else if (nums[k] < nums[right]) {
                    right = k;
                }
            }
            if (target < nums[start]) {
                start = right;
            }
            if (target > nums[end]) {
                end = left;
            }
        }
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return -1;

    }

    public static void main(String[] args) {
        Solution0033 solution = new Solution0033();
        System.out.println(solution.search(new int[] {3,5,1}, 3));
    }
}
