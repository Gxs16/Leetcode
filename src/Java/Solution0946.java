class Solution0946 {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int[] stack = new int[pushed.length];
        int j = 0;
        int k = -1;
        for (int value : pushed) {
            k++;
            stack[k] = value;
            while (k >= 0 && j < popped.length && stack[k] == popped[j]) {
                k--;
                j++;
            }
        }
        return j == popped.length;
    }
}