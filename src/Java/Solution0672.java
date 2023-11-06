import java.util.ArrayList;
import java.util.HashSet;

class Solution0672 {
    public int flipLights(int n, int presses) {
        int[] pressArray = new int[] {1<<n -1, 1<<n -1, 1<<n -1, 1<<n -1};
        for (int i = 0; i < n; i++) {
            if (i%2==0) {
                pressArray[1] ^= (1<<i);
            }
            if (i%3==1) {
                pressArray[3] ^= pressArray[1]^(1<<i);
            }
        }
        pressArray[2] = -(~pressArray[1]);
        HashSet<Integer> statusSet = new HashSet<>();
        ArrayList<HashSet<Integer>> Sets = new ArrayList<>();
        for (int press : pressArray) {
            statusSet.add(press);
        }
        Sets.add(statusSet);
        int total = presses >> 1;
        while (total > 0) {
            total >>= 1;
            Sets.add(getMultiply(Sets.get(Sets.size()-1), Sets.get(Sets.size()-1)));
        }

        HashSet<Integer> res = new HashSet<> ();
        res.add(0);
        int count = 0;
        while (presses > 0) {
            if ((presses | 1) == presses){
                res = getMultiply(res, Sets.get(count));
            }
            presses >>= 1;
            count += 1;
        }
        return res.size();
    }

    public HashSet<Integer> getMultiply (HashSet<Integer> setOne, HashSet<Integer> setTwo) {
        HashSet<Integer> res = new HashSet<>();
        for (Integer a : setOne) {
            for (Integer b : setTwo) {
                res.add(a^b);
            }
        }
        return res;
    }
}