/**
 * Definition for singly-linked list.
 */
class Solution0021 {
    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode result = new ListNode();
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        if (list1.val > list2.val) {
            result = list2;
            list2 = list2.next;
        } else {
            result = list1;
            list1 = list1.next;
        }
        ListNode current = result;
        while (list1 != null && list2 != null) {
            if (list1.val >= list2.val) {
                current.next = list2;
                list2 = list2.next;
                current = current.next;
            } else {
                current.next = list1;
                list1 = list1.next;
                current = current.next;
            }
        }
        if (list1 == null) {
            current.next = list2;
        } else {
            current.next = list1;
        }
        return result;
    }
}