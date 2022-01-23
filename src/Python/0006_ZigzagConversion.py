class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        recur = 2*numRows-2
        result = ['']*numRows
        for i, char in enumerate(s):
            idx = i % recur
            if idx >= numRows:
                result[recur-idx] += char
            else:
                result[idx] += char
        return ''.join(result)