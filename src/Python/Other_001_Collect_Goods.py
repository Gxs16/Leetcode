'''
配货员拣货，货架布局为6*6d的平面分布，下面矩阵中每个元素代表了该拣货店货物的重量
从任意一点出发，下一个拣货点和上一个拣货点是相邻的（上下左右方向）
每次捡货的重量都要比上一个货物轻，每次拣货后可以获得1元
如何设计路线能赚最多钱？
'''

import copy
import numpy as np
from collections import defaultdict

class LongestPath():
    def __init__(self):
        self.graph = defaultdict(list)
        self.reward_dict = defaultdict(list)
        self.longest_path = []

    def set_weights(self, weights):
        self.weights = weights
        self.graph = defaultdict(list)
        self.reward_dict = defaultdict(list)
        self.longest_path = []
        self._get_graph()
        self._get_reward_dict()
        self._get_answer()

    def _get_graph(self):
        '''
        获取以字典表示的图结构
        '''
        diff_vertical = self.weights[:-1] - self.weights[1:]
        diff_horizontal = self.weights[:, :-1] - self.weights[:, 1:]

        for i in range(diff_vertical.shape[0]):
            for j in range(diff_vertical.shape[1]):
                if diff_vertical[i, j] > 0:
                    self.graph[(i, j)].append((i+1, j))
                elif diff_vertical[i, j] < 0:
                    self.graph[(i+1, j)].append((i, j))
                if diff_horizontal[j, i] > 0:
                    self.graph[(j, i)].append((j, i+1))
                elif diff_horizontal[j, i] < 0:
                    self.graph[(j, i+1)].append((j, i))

        self.graph_cut = copy.deepcopy(self.graph)

    def _get_max_depth(self, coordinates):
        '''
        1.获得以每一个节点为初始节点的最大奖励值
        2.根据奖励值更新图的连通性，每个节点只会通向奖励值最大的下一个节点
        '''
        rewards = []
        nodes_keep = []
        for node in self.graph_cut[coordinates]:
            if node in self.graph_cut.keys():
                if node not in self.reward_dict.keys():
                    self._get_max_depth(node)
                rewards.append(self.reward_dict[node])
            else:
                self.reward_dict[node] = 1
                rewards.append(1)

            if self.reward_dict[node] == max(rewards):
                nodes_keep.append(node)
                
        self.reward_dict[coordinates] = max(rewards) + 1
        self.graph_cut[coordinates] = nodes_keep

    def _get_longest_path(self, nodes_list):
        path = []
        for node in nodes_list:
            if node in self.graph_cut.keys():
                path_temp = self._get_longest_path(self.graph_cut[node])
                for k in path_temp:
                    k.append(node)
                path.append()
            else:
                path.append([node])
        return path

    def _get_reward_dict(self):
        self.reward_dict = {}
        for node in self.graph_cut.keys():
            self._get_max_depth(coordinates=node)

    def _get_answer(self):
        reward_max = max(self.reward_dict.values())
        self.longest_path = []
        for node, reward in self.reward_dict.items():
            if reward == reward_max:
                longest_path_node = self._get_longest_path(self.graph_cut[node])
                for path in longest_path_node:
                    path.append(node)
                    path.reverse()
                self.longest_path.extend(longest_path_node)

    def get_longest_path(self):
        return self.longest_path

    def get_reward_dict(self):
        return self.reward_dict

    def get_num_of_path(self):
        return len(self.longest_path)



if __name__ == '__main__':
    weights1 = np.array([[32, 34, 7, 33, 21, 2],
                         [13, 12, 3, 11, 26, 36],
                         [16, 30, 22, 1, 24, 14],
                         [20, 23, 25, 5, 19, 29],
                         [27, 15, 9, 17, 31, 4],
                         [6, 18, 8, 10, 35, 28]])

    weights2 = np.array([[4, 3], [2, 1]])

    path = LongestPath()

    import time
    start = time.clock()
    for _i in range(10000):
        path.set_weights(weights1)
    end = time.clock()
    print(path.get_longest_path())
    print(path.get_num_of_path())
    print('Running time: %s Seconds'%(end-start))

    # path.set_weights(weights)
    # print(path.get_longest_path())
    # print(path.get_num_of_path())
