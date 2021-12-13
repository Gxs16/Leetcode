class Solution:
    def isPureNumber(self, s: str) -> bool:
        if s == '':
            return False
        for i in s:
            if  i < '0' or i > '9':
                return False
        return True

    def isInt(self, s: str) -> bool:
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        return self.isPureNumber(s)

    def isFloat(self, s: str) -> bool:
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        s = s.split('.')
        if len(s) > 2:
            return False
        elif len(s) == 2:
            if s[0] == '':
                return self.isPureNumber(s[1])
            if s[1] == '':
                return self.isPureNumber(s[0])
            return self.isPureNumber(s[0]) and self.isPureNumber(s[1])
        else:
            return self.isPureNumber(s[0])


    def isNumber(self, s: str) -> bool:
        if s[0] == 'e' or s[-1] == 'e' or s[0] == 'E' or s[-1] == 'E':
            return False
        for i in range(1, len(s)-1):
            if s[i] == 'e' or s[i] == 'E':
                return self.isFloat(s[0:i]) and self.isInt(s[i+1:])
        return self.isFloat(s)