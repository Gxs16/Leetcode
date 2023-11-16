import java.util.HashMap;

class Solution0020 {
    public boolean isValid(String s) {
        int[] stack = new int[s.length()];
        int j = -1;
        HashMap<Character, Character> dict = new HashMap<Character, Character>();
        dict.put(')', '(');
        dict.put(']', '[');
        dict.put('}', '{');
        for (int i=0; i < s.length();i++){
            if (s.charAt(i) == '('||s.charAt(i) == '['||s.charAt(i) == '{'){
                j++;
                stack[j] = s.charAt(i);
            }else{
                if (j>-1 && stack[j]==dict.get(s.charAt(i))){
                    j--;
                }else{
                    return false;
                }
            }
        }
        return j == -1;
    }
}