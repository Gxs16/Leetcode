import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

class Solution0652 {
    private static class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        List<TreeNode> result = new ArrayList<>();
        HashMap<String, TreeNode> map = new HashMap<>();
        HashSet<String> hasAdd = new HashSet<>();
        depthFirstSearch("", root, map, hasAdd);
        for (String code : hasAdd) {
            result.add(map.get(code));
        }
        return result;
    }

    public String depthFirstSearch(String input, TreeNode root, HashMap<String, TreeNode> map, HashSet<String> hasAdd) {
        if (root == null) {
            return input;
        } else {
            String code = depthFirstSearch("left", root.left, map, hasAdd)+String.valueOf(root.val)+depthFirstSearch("right", root.right, map, hasAdd);
            if (map.containsKey(code)) {
                hasAdd.add(code);
            } else {
                map.put(code, root);
            }
            return code;
        }
    }
}