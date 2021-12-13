class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict
        column_dict = defaultdict(list)
        row_dict = defaultdict(list)
        block_dict = defaultdict(list)
        for i in range(9):
            for j in range(9):
                block = (i//3, j//3)

                if board[i][j] != '.':
                    row_dict[i].append(board[i][j])
                    column_dict[j].append(board[i][j])
                    block_dict[block].append(board[i][j])

        self.solveUnit(board, row_dict, column_dict, block_dict, 0)

    def solveUnit(self, board, row_dict, column_dict, block_dict, start):
        for k in range(start, 81):
            i = k//9
            j = k%9
            if board[i][j] == '.':
                start = k+1
                break
        else:
            return True
        block = (i//3, j//3)
        non_available = set(row_dict[i]+column_dict[j]+block_dict[block])

        for det in [str(num) for num in range(1, 10)]:
            if not det in non_available:
                row_dict[i].append(det)
                column_dict[j].append(det)
                block_dict[block].append(det)
                
                if self.solveUnit(board, row_dict, column_dict, block_dict, start):
                    board[i][j] = det
                    return True
                else:
                    row_dict[i].pop(-1)
                    column_dict[j].pop(-1)
                    block_dict[block].pop(-1)