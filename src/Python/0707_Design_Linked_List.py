'''
@Author: Xinsheng Guo
@Time: 2020_11_26 22:23:00
@File: 0707_Design_Linked_List.py
@Link: https://leetcode-cn.com/problems/design-linked-list/
@Tag: String
'''
#%%
# class MyNode:
#     '''
#     Singly Linked List
#     '''
#     def __init__(self, value=None, nextnode=None):
#         self.value = value
#         self.next = nextnode

# class MyLinkedList:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.head = None
#         self.tail = None
#         self.count = 0


#     def get(self, index: int) -> int:
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         if index > self.count-1:
#             return -1
#         elif index == self.count-1:
#             return self.tail.value
#         else:
#             i = 0
#             node = self.head
#             while i <= index:
#                 value = node.value
#                 node = node.next
#                 i+=1
#             return value

#     def addAtHead(self, val: int) -> None:
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         """
#         if self.head:
#             new_node = MyNode(val, self.head)
#             self.head = new_node
#         else:
#             new_node = MyNode(value=val)
#             self.head = new_node
#             self.tail = new_node
#         self.count += 1

#     def addAtTail(self, val: int) -> None:
#         """
#         Append a node of value val to the last element of the linked list.
#         """
#         if self.tail:
#             new_node = MyNode(val)
#             self.tail.next = new_node
#             self.tail = new_node
#         else:
#             new_node = MyNode(value=val)
#             self.head = new_node
#             self.tail = new_node
#         self.count += 1


#     def addAtIndex(self, index: int, val: int) -> None:
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         """
#         if index == self.count:
#             self.addAtTail(val)
#         elif index == 0:
#             self.addAtHead(val)
#         elif index > self.count:
#             pass
#         else:
#             i = 0
#             node = self.head
#             while i < index-1:
#                 node = node.next
#                 i+=1
#             new_node = MyNode(val, node.next)
#             node.next = new_node
#             self.count += 1

#     def deleteAtIndex(self, index: int) -> None:
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         if index >= self.count:
#             pass
#         elif index == 0:
#             self.head = self.head.next
#             self.count -= 1
#         else:
#             i = 0
#             node = self.head
#             while i < index-1:
#                 node = node.next
#                 i += 1
#             node.next = node.next.next
#             if index == self.count-1:
#                 self.tail = node
#             self.count -= 1

#%%
a = MyLinkedList()
a.addAtHead(1)
a.addAtTail(3)
#%%
a.addAtIndex(1, 2)
print(a.get(1))
a.deleteAtIndex(2)
print(a.get(1))

# %%
a = MyLinkedList()
a.addAtHead(0)
a.addAtIndex(1,4)
a.addAtTail(8)
a.addAtHead(5)
a.addAtIndex(4,3)
a.addAtTail(0)
a.addAtTail(5)
a.addAtIndex(6,3)
a.deleteAtIndex(7)
a.deleteAtIndex(5)
a.addAtTail(4)

# %%
class MyNode:
    '''
    Doubly Linked List
    '''
    def __init__(self, value=None, nextnode=None, prevnode=None):
        self.value = value
        self.next = nextnode
        self.prev = prevnode

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = MyNode()
        self.tail = MyNode(prevnode=self.head)
        self.head.next = self.tail
        self.count = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.count-1:
            return -1
        elif index == self.count-1:
            return self.tail.prev.value
        else:
            if self.count-1-index >= index:
                i = 0
                node = self.head.next
                while i <= index:
                    node = node.next
                    i += 1
                return node.prev.value
            else:
                i = self.count-1
                node = self.tail.prev
                while i >= index:
                    node = node.prev
                    i -= 1
                return node.next.value

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = MyNode(value=val, prevnode=self.head, nextnode=self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.count += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = MyNode(value=val, nextnode=self.tail, prevnode=self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.count += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == self.count:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif index > self.count:
            pass
        else:
            if self.count-1-index >= index:
                i = 0
                node = self.head.next
                while i < index-1:
                    node = node.next
                    i += 1
                new_node = MyNode(val, node.next, node)
                node.next.prev = new_node
                node.next = new_node
            else:
                i = self.count-1
                node = self.tail.prev
                while i > index:
                    node = node.prev
                    i -= 1
                new_node = MyNode(val, node, node.prev)
                node.prev.next = new_node
                node.prev = new_node
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.count:
            pass
        elif index == 0:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.count -= 1
        elif index == self.count-1:
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.count -= 1
        else:
            if self.count-1-index >= index:
                i = 0
                node = self.head.next
                while i < index-1:
                    node = node.next
                    i += 1
                node.next = node.next.next
                node.next.prev = node
            else:
                i = self.count-1
                node = self.tail.prev
                while i > index+1:
                    node = node.prev
                    i -= 1
                node.prev = node.prev.prev
                node.prev.next = node
            self.count -= 1
# %%
# 4/48
a = MyLinkedList()
a.addAtHead(1)
a.addAtTail(3)
a.addAtIndex(1,2)
a.get(1)
a.deleteAtIndex(0)
a.get(0)
# %%
# 23/58
a = MyLinkedList()
a.addAtIndex(0,10)
a.addAtIndex(0,20)
a.addAtIndex(1,30)
a.get(0)
# %%
