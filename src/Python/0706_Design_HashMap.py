'''
@Author: Xinsheng Guo
@Time: 2020-12-18 17:25:40
@File: 0706_Design_HashMap.py
@Link: https://leetcode-cn.com/problems/design-hashmap/
@Tag: Design; Hash Map
'''
#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#
#%%
# @lc code=start
class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class Bracket:
    def __init__(self, length):
        self.bracket_list = [[] for i in range(length)]

    def add(self, index, key, val):
        if self.bracket_list[index]:
            node = self.bracket_list[index]
            while node:
                if node.key == key:
                    node.value = val
                    break
                node = node.next
            else:
                node = Node(key=key, value=val)
        else:
            self.bracket_list[index] = Node(key=key, value=val)
            
    def get(self, index, key):
        if self.bracket_list[index]:
            node = self.bracket_list[index]
            while node:
                if node.key == key:
                    return node.value
                node = node.next
        else:
            return -1

    def remove(self, index, key):
        if self.bracket_list[index]:
            node = self.bracket_list[index]
            while node.next:
                if node.next.key == key:
                    node.next = node.next.next
                    break
                else:
                    node = node.next
                    
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 10000
        self.bracket = Bracket(self.length)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key%self.length
        self.bracket.add(index, key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key%self.length
        return self.bracket.get(index, key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key%self.length
        self.bracket.remove(index, key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
#%%
a = MyHashMap()
a.put(1,1)
a.put(2,2)
a.get(1)
a.get(3)
a.put(2,1)
a.get(2)
a.remove(2)
a.get(2)