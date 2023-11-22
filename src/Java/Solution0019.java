
class Solution0019 {

    public static class ListNode {
        ListNode next;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length = 1;
        ListNode left = head;
        ListNode right = head;
        while (right.next != null) {
            length++;
            right = right.next;
        }
        if (length == 1) {
            return null;
        }
        if (length == n) {
            return head.next;
        }
        while (length > n + 1) {
            left = left.next;
            length -= 1;
        }
        left.next = left.next.next;
        return head;
    }
}
