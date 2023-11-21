import java.util.HashSet;
import java.util.Set;

class Solution0128 {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int i : nums) {
            numSet.add(i);
        }
        int length = 0;
        for (int i : numSet) {
            if (numSet.contains(i - 1)) {
                continue;
            } else {
                int tmp = i;
                while (numSet.contains(tmp)) {
                    tmp += 1;
                }
                length = Math.max(length, tmp - i);
            }
        }
        return length;
    }
}