import java.util.ArrayList;
import java.util.List;

class Solution0054 {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>(matrix.length * matrix[0].length);
        int direction = 0;
        int i = 0;
        int j = 0;
        int upperBound = 0;
        int lowerBound = matrix.length - 1;
        int leftBound = 0;
        int rightBound = matrix[0].length - 1;
        while (res.size() < matrix.length * matrix[0].length) {
            res.add(matrix[i][j]);
            if (direction == 0) {
                if (j < rightBound) {
                    j += 1;
                } else {
                    i += 1;
                    direction = 1;
                    upperBound += 1;
                }
            } else if (direction == 1) {
                if (i < lowerBound) {
                    i += 1;
                } else {
                    j -= 1;
                    direction = 2;
                    rightBound -= 1;
                }
            } else if (direction == 2) {
                if (j > leftBound) {
                    j -= 1;
                } else {
                    i -= 1;
                    direction = 3;
                    lowerBound -= 1;
                }
            } else {
                if (i > upperBound) {
                    i -= 1;
                } else {
                    j += 1;
                    direction = 0;
                    leftBound += 1;
                }
            }
        }
        return res;
    }
}
