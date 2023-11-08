class Solution0098 {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public int[] dfs(TreeNode root) {
        int[] res = new int[3];
        res[1] = root.val;
        res[2] = root.val;
        boolean isValid = true;
        if (root.left != null) {
            int[] resLeft = dfs(root.left);
            isValid = resLeft[2] < root.val && resLeft[0] == 1;
            res[1] = Math.min(root.val, resLeft[1]);
        }
        if (root.right != null) {
            int[] resRight = dfs(root.right);

            isValid = isValid && resRight[1] > root.val && resRight[0] == 1;
            res[2] = Math.max(root.val, resRight[2]);
        }
        if (isValid) {
            res[0] = 1;
        }
        return res;
    }

    public boolean isValidBST(TreeNode root) {
        int[] res = dfs(root);
        return res[0] == 1;
    }
}

