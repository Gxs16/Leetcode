class Solution:
    def numDecodings(self, s: str) -> int:
        map_dict = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                    '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'}
        result = 0
        result_p = 0
        if s[0] == '0':
            return 0
        else:
            result_p = 1
        if len(s) == 1:
            return result_p
        if s[1] in map_dict:
            result = result_p
        if s[0:2] in map_dict:
            result += 1
        for i in range(2, len(s)):
            num = s[i]
            if s[i] in map_dict and s[i-1:i+1] in map_dict:
                tmp = result_p
                result_p = result
                result += tmp
            elif s[i] in map_dict and s[i-1:i+1] not in map_dict:
                pass
            elif s[i] not in map_dict and s[i-1:i+1] in map_dict:
                tmp = result_p
                result_p = result
                result = tmp
            else:
                return 0
        return result