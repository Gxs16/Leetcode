class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        column_dict = {}
        row_dict = {}
        block_dict = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if i in row_dict:
                        row_dict[i].append(board[i][j])
                    else:
                        row_dict[i] = [board[i][j]]

                    if j in column_dict:
                        column_dict[j].append(board[i][j])
                    else:
                        column_dict[j] = [board[i][j]]

                    block = (i//3, j//3)
                    if block in block_dict:
                        block_dict[block].append(board[i][j])
                    else:
                        block_dict[block] = [board[i][j]]

        self.solveUnit(board, row_dict, column_dict, block_dict, 0, 0)

    def getStart(self, board, row_start, column_start):
        for i in range(row_start, 9):
            for j in range(column_start, 9):
                if board[i][j] == '.':
                    return i, j
        return None, None

    def solveUnit(self, board, row_dict, column_dict, block_dict, row_start, column_start):
        i, j = self.getStart(board, row_start, column_start)
        if i == None:
            return True
        block = (i//3, j//3)
        non_available = row_dict[i]+column_dict[j]+block_dict[block]
        available = []
        for num in range(1, 10):
            if not str(num) in non_available:
                available.append(str(num))
        if available:
            board_next = board.copy()
            for det in available:
                row_dict_next = row_dict.copy()
                column_dict_next = column_dict.copy()
                block_dict_next = block_dict.copy()
                row_dict_next[i].append(det)
                column_dict_next[j].append(det)
                block_dict_next[block].append(det)
                board_next[i][j] = det
                if self.solveUnit(board_next, row_dict_next, column_dict_next, block_dict_next, i, j):
                    board = board_next
                    return True
        else:
            return False