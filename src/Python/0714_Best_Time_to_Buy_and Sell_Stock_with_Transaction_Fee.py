class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        state1, state2 = -prices[0], 0
        for v in prices:
            state1 = max(state2-v, state1)
            state2 = max(state2, state1+v-fee)
        return state2