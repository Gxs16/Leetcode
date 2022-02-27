class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        map_dict = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        sums = 0
        index_dict = {0:-1}
        result = 0
        for i in range(len(s)):
            if s[i] in map_dict:
                sums = sums^(1<<map_dict[s[i]])
            if sums not in index_dict:
                index_dict[sums] = i
            result = max(result, i-index_dict[sums])
        return result