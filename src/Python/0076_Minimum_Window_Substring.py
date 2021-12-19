class Solution:
    def compare(self, s_dict, t_dict):
        for i in t_dict:
            if i not in s_dict or s_dict[i] < t_dict[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        result = (0, 0)
        t_dict = {}
        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 1
        s_dict = {}
        for start in range(len(s)):
            if s[start] in t_dict:
                break
        right = start
        left = start-1
        for right in range(start, len(s)):
            if s[right] in t_dict:
                if s[right] in s_dict:
                    s_dict[s[right]] += 1
                else:
                    s_dict[s[right]] = 1
                if self.compare(s_dict, t_dict):
                    result = (left, right)
                    break
        else:
            return ''

        while left < right-len(t):
            left += 1
            if s[left] in t_dict:
                s_dict[s[left]] -= 1
                if s_dict[s[left]] < t_dict[s[left]]:
                    while right < len(s)-1:
                        right += 1
                        if s[right] in s_dict:
                            s_dict[s[right]] += 1
                            if s[right] == s[left]:
                                if right-left < result[1]-result[0]:
                                    result = (left, right)
                                break
                    else:
                        break
                else:
                    if right-left < result[1]-result[0]:
                        result = (left, right)
            else:
                if right-left < result[1]-result[0]:
                    result = (left, right)

        while left < len(s)-len(t)-1:
            left += 1
            if s[left] in t_dict:
                s_dict[s[left]] -= 1
                if self.compare(s_dict, t_dict):
                    if right-left < result[1]-result[0]:
                        result = (left, right)
        
        return s[result[0]+1: result[1]+1]
        
