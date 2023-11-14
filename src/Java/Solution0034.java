import java.util.Arrays;

public class Solution0034 {
    public int[] searchRange(int[] nums, int target) {
        int tmp = binarySearch(nums, 0, nums.length-1, target);
        if (tmp == -1) {
            return new int[] {-1, -1};
        } else {
            int start;
            int mid = tmp;
            while (true) {
                start = binarySearch(nums, 0, mid, target);
                if (start == mid) {
                    break;
                } else {
                    mid = start;
                }
            }
            mid = tmp;
            int end;
            while (true) {
                end = binarySearchRight(nums, mid, nums.length-1, target);
                if (end == mid) {
                    break;
                } else {
                    mid = end;
                }
            }
            return new int[] {start, end};
        }
    }
    public int binarySearch(int[] nums, int left, int right, int target) {
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
    public int binarySearchRight(int[] nums, int left, int right, int target) {

        while (left <= right) {
            int mid = right - (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution0034 solution = new Solution0034();
        System.out.println(Arrays.toString(solution.searchRange(new int[]{6, 6}, 6)));
    }
}
