class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        if not prices:
            return 0
        state = [[[float('-inf'), 0] for i in range(k)] for j in prices]
        for i, v in enumerate(prices):
            state[i][0][0] = max(-v, state[i-1][0][0])
            state[i][0][1] = max(state[i][0][0]+v, state[i-1][0][1])
            for j in range(1, k):
                state[i][j][0] = max(state[i][j-1][1]-v, state[i-1][j][0])
                state[i][j][1] = max(state[i][j][0]+v, state[i-1][j][1])
        return state[-1][-1][-1]

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        if not prices:
            return 0
        state = [[float('-inf'), 0] for i in range(k)]
        for i, v in enumerate(prices):
            state[0][0] = max(-v, state[0][0])
            state[0][1] = max(state[0][0]+v, state[0][1])
            for j in range(1, k):
                state[j][0] = max(state[j-1][1]-v, state[j][0])
                state[j][1] = max(state[j][0]+v, state[j][1])
        return state[-1][-1]