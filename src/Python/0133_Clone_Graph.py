'''
@Author: Xinsheng Guo
@Time: 2020-11-29 18:13:34
@File: 0133_Clone_Graph.py
@Link: https://leetcode-cn.com/problems/clone-graph/
@Tag: Graph; Depth-first Search; Breadth-first Search
'''

from copy import deepcopy
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        node_new = deepcopy(node)
        stack = []
        node_set = {node}
        while stack:
            x = stack.pop()
            _list = []
            for i in x.neighbors:
                a = deepcopy(i)
                _list.append(a)
                if not i in node_set:
                    node_set.add(i)
                    stack.append(i)
            x.neighbors = _list
        return node_new
            