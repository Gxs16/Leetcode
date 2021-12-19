class Solution:
    def maximalRectangle(self, matrix) -> int:
        total_result = 0
        right_max = {}
        bottom_max = {}
        rows_num = len(matrix)
        columns_num = len(matrix[0])
        for row, _row in enumerate(matrix):
            for column, _column in enumerate(matrix[row]):
                if matrix[row][column] == '1':
                    if (row, column) not in bottom_max:
                        bottom = row+1
                        while bottom < rows_num and matrix[bottom][column] == '1':
                            bottom += 1
                        for i in range(row, bottom):
                            bottom_max[(i, column)] = bottom
                    if (row, column) not in right_max:
                        right = column+1
                        while right < columns_num and matrix[row][right] == '1':
                            right += 1
                        for j in range(column, right):
                            right_max[(row, j)] = right

        for row, column in bottom_max:
            right_min = columns_num
            for bottom in range(row, bottom_max[(row, column)]):
                right_min = min(right_max[(bottom, column)], right_min)
                total_result= max(total_result, (right_min-column)*(bottom-row+1))
        return total_result