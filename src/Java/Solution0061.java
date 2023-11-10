


class Solution0061 {
    public static class ListNode {
        int val;
        ListNode next;

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode rotateRight(ListNode head, int k) {
        if (k == 0 || head == null) return head;
        int length = 1;
        ListNode tail = head;
        while (tail.next != null) {
            tail = tail.next;
            length++;
        }
        k = k % length;
        if (k == 0) return head;
        ListNode left = head;
        for (int i = 1; i < length - k; i++) {
            left = left.next;
        }
        tail.next = head;
        head = left.next;
        left.next = null;
        return head;

    }
}
