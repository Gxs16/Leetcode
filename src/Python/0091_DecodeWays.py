class Solution:
    def numDecodings(self, s: str) -> int:
        map_dict = {str(i) for i in range(1, 27)}
        result_p = 1
        if s[0] == '0':
            return 0
        else:
            result = 1
        for i in range(1, len(s)):
            if s[i-1:i+1] in map_dict:
                tmp = result_p
                result_p = result
                if s[i] in map_dict:
                    result += tmp
                else:
                    result = tmp
            else:
                if s[i] in map_dict:
                    result_p = result
                else:
                    return 0
        return result