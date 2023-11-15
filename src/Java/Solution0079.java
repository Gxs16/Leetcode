class Solution0079 {

    public boolean exist(char[][] board, String word) {
        boolean res = false;
        boolean[] path = new boolean[board.length * board[0].length];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0)) {
                    path[i * board[0].length + j] = true;
                    res = res || dfs(board, word, 1, path, i, j);
                    path[i * board[0].length + j] = false;
                }
            }
        }
        return res;
    }

    public boolean dfs(char[][] board, String word, int target, boolean[] path, int i, int j) {
        if (target == word.length()) {
            return true;
        }
        boolean res = false;
        if (i > 0) {
            if (word.charAt(target) == board[i - 1][j] && !path[(i - 1) * board[0].length + j]) {
                path[(i - 1) * board[0].length + j] = true;
                res = dfs(board, word, target + 1, path, i - 1, j);
                path[(i - 1) * board[0].length + j] = false;
            }
        }
        if (j > 0) {
            if (word.charAt(target) == board[i][j - 1] && !path[(i) * board[0].length + j - 1]) {
                path[(i) * board[0].length + j - 1] = true;
                res = res || dfs(board, word, target + 1, path, i, j - 1);
                path[(i) * board[0].length + j - 1] = false;
            }
        }
        if (i < board.length - 1) {
            if (word.charAt(target) == board[i + 1][j] && !path[(i + 1) * board[0].length + j]) {
                path[(i + 1) * board[0].length + j] = true;
                res = res || dfs(board, word, target + 1, path, i + 1, j);
                path[(i + 1) * board[0].length + j] = false;
            }
        }
        if (j < board[0].length - 1) {
            if (word.charAt(target) == board[i][j + 1] && !path[i * board[0].length + j + 1]) {
                path[i * board[0].length + j + 1] = true;
                res = res || dfs(board, word, target + 1, path, i, j + 1);
                path[i * board[0].length + j + 1] = false;
            }
        }
        return res;
    }

}