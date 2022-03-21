class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal:
            return False
        def dfs(state, state_dict, current_sum):
            if state_dict[state] is not None:
                return state_dict[state]
            for i in range(maxChoosableInteger):
                if 1<<i & state == 0:
                    if current_sum+i+1 >= desiredTotal or not dfs(state|1<<i, state_dict, current_sum+i+1):
                        state_dict[state] = True
                        state_dict[state|1<<i] = False
                        return True
            state_dict[state] = False
            return False
        return dfs(0, [None]*(1<<maxChoosableInteger), 0)