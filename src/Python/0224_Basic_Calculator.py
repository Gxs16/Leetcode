class Solution:
    def calculate_list(self, l: list):
        total = 0
        multi = 1
        for ele in l:
            if ele == '+':
                multi = 1
            elif ele == '-':
                multi = -1
            else:
                total += multi*ele
        return total

    def pop_until_leftpar(self, stack):
        ele = stack.pop()
        result = 0
        num = 0
        while ele != '(':
            if ele == '+':
                result += num
                num = 0
            elif ele == '-':
                result -= num
                num = 0
            else:
                num = ele
            ele = stack.pop()
        result += num
        stack.append(result)

    def calculate(self, s: str) -> int:
        num = ''
        stack = []
        for char in s:
            if char == ' ':
                continue
            elif char == '(':
                stack.append(char)
            elif char == ')':
                if num:
                    stack.append(int(num))
                    num = ''
                self.pop_until_leftpar(stack)
            elif char in {'+', '-'}:
                if num:
                    stack.append(int(num))
                    num = ''
                stack.append(char)
            else:
                num += char
        if num:
            stack.append(int(num))
        return self.calculate_list(stack)
