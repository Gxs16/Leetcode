class Solution0739 {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        int[][] stack = new int[temperatures.length][2];
        int top = -1;
        for (int i = 1; i < res.length; i++) {
            if (temperatures[i] > temperatures[i - 1]) {
                res[i - 1] = 1;
            } else {
                top += 1;
                stack[top] = new int[]{temperatures[i - 1], i - 1};
            }
            while (top > -1) {
                if (temperatures[i] > stack[top][0]) {
                    res[stack[top][1]] = i - stack[top][1];
                    top -= 1;
                } else {
                    break;
                }
            }
        }
        return res;
    }
}
