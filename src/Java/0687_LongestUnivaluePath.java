/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int longestUnivaluePath(TreeNode root) {
        if (root == null) return 0;
        return findPath(root)[0];
    }

    public int[] findPath(TreeNode root) {
        int[] res = new int[]{0, -1};
        int[] leftRes = new int[2];
        int[] rightRes = new int[2];
        if (root.left != null) {
            leftRes = findPath(root.left);
            if (root.val == root.left.val) {
                res[1] = Math.max(res[1], leftRes[1]);
                res[0] += (leftRes[1]+1);
            }
        }

        if (root.right != null) {
            rightRes = findPath(root.right);
            if (root.val == root.right.val) {
                res[1] = Math.max(res[1], rightRes[1]);
                res[0] += (rightRes[1]+1);
            }
        }
        res[1] += 1;
        res[0] = Math.max(res[0], Math.max(leftRes[0], rightRes[0]));
        return res;
    }
}
