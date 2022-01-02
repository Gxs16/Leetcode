class Solution:
    def checkValid(self, s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
        return stack

    def remove(self, needremove, stack, prefix, suffix, result):
        stack = stack.copy()
        if needremove:
            for i, char in enumerate(suffix):
                if char == needremove[0] and (i == 0 or char != suffix[i-1]):
                        self.remove(needremove[1:], stack, prefix+suffix[0:i], suffix[i+1:], result)
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        break
        else:
            for char in suffix:
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return None
            if not stack:
                result.append(prefix+suffix)

    def removeInvalidParentheses(self, s: str):
        if len(s) < 1:
            return ['']
        else:
            needremove = self.checkValid(s)
            if needremove:
                result = []
                stack = []
                self.remove(needremove, stack, '', s, result)
                return result
            else:
                return [s]