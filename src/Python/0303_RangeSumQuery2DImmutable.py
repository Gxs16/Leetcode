class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = [[0]*(len(matrix[0])+1)]
        for i in range(len(matrix)):
            _result = [0]
            result = [0]
            for j in range(len(matrix[i])):
                _result.append(_result[-1]+matrix[i][j])
                result.append(_result[j+1]+self.sums[i][j+1])
            self.sums.append(result)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1]+self.sums[row1][col1]-self.sums[row1][col2+1]-self.sums[row2+1][col1]
