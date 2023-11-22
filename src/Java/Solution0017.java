import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

class Solution0017 {
    public List<String> letterCombinations(String digits) {

        HashMap<Character, String[]> relation = new HashMap<>();
        relation.put('2', new String[]{"a", "b", "c"});
        relation.put('3', new String[]{"d", "e", "f"});
        relation.put('4', new String[]{"g", "h", "i"});
        relation.put('5', new String[]{"j", "k", "l"});
        relation.put('6', new String[]{"m", "n", "o"});
        relation.put('7', new String[]{"p", "q", "r", "s"});
        relation.put('8', new String[]{"t", "u", "v"});
        relation.put('9', new String[]{"w", "x", "y", "z"});

        LinkedList<String> res = new LinkedList<>();
        for (int i = 0; i < digits.length(); i++) {
            if (res.isEmpty()) {
                res.addAll(Arrays.asList(relation.get(digits.charAt(i))));
            }
            while (res.get(0).length() < i + 1) {
                String tmp = res.removeFirst();
                for (String j : relation.get(digits.charAt(i))) {
                    res.add(tmp + j);
                }
            }
        }
        return res;

    }
}
