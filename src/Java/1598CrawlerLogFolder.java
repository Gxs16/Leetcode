class Solution {
    public int minOperations(String[] logs) {
        int step = 0;
        for (String operation : logs) {
            if ("../".equals(operation)) {
                if (step == 0) {
                    continue;
                } else {
                    step -= 1;
                    continue;
                }
            }
            if ("./".equals(operation)) {
                continue;
            }
            step += 1;
        }
        return step;
    }
}