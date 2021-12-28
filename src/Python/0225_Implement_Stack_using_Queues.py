'''
@Author: Xinsheng Guo
@Time: 2021年1月29日14:25:49
@File: 0225_Implement_Stack_using_Queues.py
@Link: https://leetcode-cn.com/problems/implement-stack-using-queues/
@Tag: Stack; Design; Queue
'''
#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        _data = []
        length = len(self.data)
        while len(_data) < length - 1:
            _data.append(self.data.pop(0))
        result = self.data[0]
        self.data = _data
        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        _data = []
        length = len(self.data)
        while len(_data) < length - 1:
            _data.append(self.data.pop(0))
        result = self.data[0]
        _data.append(result)
        self.data = _data
        return result

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.data) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
#%%
a = [0,1,2,3]
a.pop(0)

# %%
