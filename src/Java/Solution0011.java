import java.util.LinkedList;
import java.util.List;

class Solution0011 {
    public int maxArea(int[] height) {
        int res = 0;
        int[] pos = new int[height.length];
        int flag = 0;
        for (int i = 1; i < height.length; i++) {

            for (int j = 0; j <= flag; j++) {
                res = Math.max(res, Math.min(height[pos[j]], height[i]) * (i - pos[j]));
            }
            if (height[i] > height[pos[flag]]) {
                flag += 1;
                pos[flag] = i;
            }

        }
        return res;
    }
}