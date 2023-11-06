class Solution1598 {
    public int minOperations(String[] logs) {
        int step = 0;
        for (String operation : logs) {
            if ("../".equals(operation)) {
                if (step != 0) {
                    step -= 1;
                }
                continue;
            }
            if ("./".equals(operation)) {
                continue;
            }
            step += 1;
        }
        return step;
    }
}