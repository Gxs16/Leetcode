class Solution {
    public int numSpecial(int[][] mat) {
        int[] resColumn = new int[mat.length];
        int[] resRow = new int[mat[0].length];
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j ++) {
                resColumn[i] += mat[i][j];
                resRow[j] += mat[i][j];
            }
        }
        int count = 0;
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j ++) {
                if (mat[i][j] == 1 && resColumn[i] == 1 && resRow[j] == 1) {
                    count ++;
                }
            }
        }
        return count;
    }
}