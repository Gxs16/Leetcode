import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

class Solution0078 {
    public List<List<Integer>> subsets(int[] nums) {
        int[] record = new int[(int) Math.pow(2, nums.length)];
        HashSet<Integer> records = new HashSet<>();
        List<List<Integer>> res = new ArrayList<>((int) Math.pow(2, nums.length));
        res.add(new ArrayList<>());

        Arrays.fill(record, 0);
        records.add(0);
        int j = 1;
        int end = 0;
        for (int i = 0; i < nums.length; i++) {
            int start = end;
            end = j;
            for (int num : nums) {
                for (int k = start; k < end; k++) {
                    List<Integer> subset = res.get(k);
                    int pattern = (record[k] | (1 << (num + 10)));
                    if (pattern != record[k] && !records.contains(pattern)) {
                        records.add(pattern);
                        record[j] = pattern;
                        res.add(new ArrayList<>(subset));
                        res.get(j).add(num);
                        j++;
                    }
                }
            }
        }
        return res;
    }
}