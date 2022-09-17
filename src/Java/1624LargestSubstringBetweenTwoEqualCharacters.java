class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        char[] chars = s.toCharArray();
        HashMap<Character, Integer> position = new HashMap<> ();
        int res = -1;
        for (int i = 0; i < chars.length; i ++) {
            if (position.containsKey(chars[i])) {
                if (i-position.get(chars[i])-1 > res) {
                    res = i-position.get(chars[i])-1;
                }
            } else {
                position.put(chars[i], i);
            }
        }
        return res;
    }
}