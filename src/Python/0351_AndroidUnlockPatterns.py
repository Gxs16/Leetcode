class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        from collections import defaultdict
        available_bin = {0: 186, 1: 381, 2: 186, 3: 471, 4: 495, 5: 471, 6: 186, 7: 381, 8: 186}
        available_add = {0:{2:4, 8:64, 16:256},
                         1:{16:128},
                         2:{2:1, 32:256, 16:64},
                         3:{16:32},
                         4:{},
                         5:{16:8},
                         6:{8:1, 16:4, 128:256},
                         7:{16:2},
                         8:{32:4, 16:1, 128:64}}
        dp = [[defaultdict(int) for i in range(9)] for j in range(n)]
        for i in range(9):
            dp[0][i][1<<i] = 1
        for i in range(1, n):
            for j in range(9):
                for k in range(9):
                    if k != j:
                        for l in dp[i-1][k].keys():
                            next_avai = available_bin[k]
                            for o,p in available_add[k].items():
                                if o|l == l:
                                    next_avai |= p
                            next_avai = next_avai ^ (next_avai & l)
                            if (next_avai | (1<<j)) == next_avai:
                                dp[i][j][l|(1<<j)] += dp[i-1][k][l]
        result = 0
        for i in range(m-1, n):
            for j in range(9):
                result += sum(dp[i][j].values())
        return result

