class Solution:
    def myAtoi(self, s: str) -> int:
        # 'SYM', 'NUM', 'SPACE', 'CHAR'
        state = 'SPACE'
        is_num = False
        for i, char in enumerate(s):
            if char == ' ':
                if state == 'NUM' or state == 'SYM':
                    state = 'SPACE'
                    break
            elif char == '-' or char == '+':
                if state == 'SPACE':
                    state = 'SYM'
                else:
                    state = 'SYM'
                    break
            elif ord(char) <= 57 and ord(char) >= 48:
                is_num = True
                state = 'NUM'
            else:
                state = 'CHAR'
                break
        if is_num:
            if state == 'NUM':
                res = int(s)
            else:
                res = int(s[:i])
            res = max(res, -2**31)
            res = min(res, 2**31-1)
        else:
            res = 0
        return res