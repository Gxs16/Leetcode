class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        state = [[float('-inf'), 0] for i in range(len(prices)+1)]
        for i, v in enumerate(prices):
            state[i+1][0] = max(state[i-1][1]-v, state[i][0])
            state[i+1][1] = max(state[i][1], state[i][0]+v)
        return state[-1][1]