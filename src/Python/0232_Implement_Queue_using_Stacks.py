'''
@Author: Xinsheng Guo
@Time: 2021年1月18日 11:43:19
@File: 0232_Implement_Queue_using_Stacks.py
@Link: https://leetcode-cn.com/problems/implement-queue-using-stacks/
@Tag: Stack; Design
'''
#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyStack:
    def __init__(self):
        self.data = []
        
    def push(self, x: int) -> None:
        self.data.append(x)
        
    def pop(self) -> int:
        if self.data:
            return self.data.pop()
        else:
            raise Exception('Stack is empty!')
    
    def is_empty(self) -> bool:
        if self.data:
            return False
        else:
            return True
    
    def peek(self) -> int:
        if self.data:
            return self.data[-1]
        else:
            raise Exception('Stack is empty!')

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = MyStack()
        self.stack2 = MyStack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2.is_empty():
            if not self.stack1.is_empty():
                while not self.stack1.is_empty():
                    self.stack2.push(self.stack1.pop())
            else:
                raise Exception('Queue is empty!')
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2.is_empty():
            if not self.stack1.is_empty():
                while not self.stack1.is_empty():
                    self.stack2.push(self.stack1.pop())
            else:
                raise Exception('Queue is empty!')
        return self.stack2.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack1.is_empty() and self.stack2.is_empty():
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

