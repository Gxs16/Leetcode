public class Solution0071 {
    public String simplifyPath(String path) {
        String[] folders = path.split("/");
        String[] stack = new String[folders.length];
        int top = 0;
        for (String folder : folders) {
            if ("".equals(folder)) {
                continue;
            } else if (".".equals(folder)) {
                continue;
            } else if ("..".equals(folder)) {
                if (top > 0) {
                    top -= 1;
                }
                continue;
            }
            stack[top] = folder;
            top += 1;
        }
        StringBuilder res = new StringBuilder();

        for (int i = 0; i < top; i ++) {
            res.append(stack[i]);
            res.append("/");
        }
        if (res.length() > 0) {
            res.delete(res.length()-1, res.length());
        }
        res.insert(0, "/");
        return res.toString();
    }

    public static void main(String[] args) {
        Solution0071 solution = new Solution0071();
        System.out.println(solution.simplifyPath("/home//foo////"));
    }
}
