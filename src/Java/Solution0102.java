import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;


class Solution0102 {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public List<List<Integer>> levelOrder(TreeNode root) {
        LinkedList<List<TreeNode>> queue = new LinkedList<>();
        ArrayList<TreeNode> tmp = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        tmp.add(root);
        queue.add(tmp);

        while (!queue.isEmpty()) {
            List<TreeNode> nodes = queue.pop();
            List<TreeNode> nodesAdd = new ArrayList<>(nodes.size() * 2);
            List<Integer> vals = new ArrayList<>(nodes.size());
            for (TreeNode node : nodes) {
                vals.add(node.val);
                if (node.left != null) {
                    nodesAdd.add(node.left);
                }
                if (node.right != null) {
                    nodesAdd.add(node.right);
                }
            }
            if (!nodesAdd.isEmpty()) {
                queue.add(nodesAdd);

            }
            res.add(vals);
        }
        return res;
    }
}
