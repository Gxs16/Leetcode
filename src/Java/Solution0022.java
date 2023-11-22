import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class Solution0022 {
    public List<String> generateParenthesis(int n) {
        List<String> res = new LinkedList<>();
        List<String> pattern = new ArrayList<>(2 * n);
        dfs(res, n, n, pattern);
        return res;

    }

    public void dfs(List<String> res, int left, int right, List<String> pattern) {
        if (left == 0 && right == 0) {
            StringBuilder sb = new StringBuilder();
            for (String s : pattern) {
                sb.append(s);
            }
            res.add(sb.toString());
        } else {
            if (left <= right) {
                if (left > 0) {
                    pattern.add("(");
                    dfs(res, left - 1, right, pattern);
                    pattern.remove(pattern.size() - 1);
                }
                pattern.add(")");
                dfs(res, left, right - 1, pattern);
                pattern.remove(pattern.size() - 1);
            }
        }
    }
}