import java.util.HashMap;

class Solution0003 {
    public int lengthOfLongestSubstring(String s) {
        int left = -1;
        HashMap<Character, Integer> stringToIndex= new HashMap<>();
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            char target = s.charAt(i);
            if (stringToIndex.containsKey(target)) {
                left = Math.max(stringToIndex.get(target), left);
            }
            res = Math.max(res, i-left);
            stringToIndex.put(target, i);
        }
        return res;
    }}