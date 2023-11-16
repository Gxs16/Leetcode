class Solution0002 {
    public static class ListNode {
        int val;
        ListNode next;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int add = 0;
        ListNode res = new ListNode(-1);
        ListNode current = res;
        while (l1 != null && l2 != null) {
            int val = add + l1.val + l2.val;
            if (val >= 10) {
                val -= 10;
                add = 1;
            } else {
                add = 0;
            }
            current.next = new ListNode(val);
            current = current.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        if (l1 == null && l2 != null) {
            if (add > 0) {
                while (l2 != null) {
                    int val = l2.val + add;
                    if (val >= 10) {
                        val -= 10;
                    } else {
                        add = 0;
                    }
                    current.next = new ListNode(val);
                    current = current.next;
                    l2 = l2.next;
                }
            } else {
                current.next = l2;
                return res.next;
            }
        }
        if (l1 != null) {
            if (add > 0) {
                while (l1 != null) {
                    int val = l1.val + add;
                    if (val >= 10) {
                        val -= 10;
                    } else {
                        add = 0;
                    }
                    current.next = new ListNode(val);
                    current = current.next;
                    l1 = l1.next;
                }
            } else {
                current.next = l1;
                return res.next;
            }
        }
        if (add > 0) {
            current.next = new ListNode(add);
        }
        return res.next;
    }
}
