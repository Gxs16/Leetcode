class Solution {
    public String longestCommonPrefix(String[] strs) {
        String result = "";
        boolean stop = false;
        int i = 0;
        while (!stop){
            if (i == strs[0].length()){
                stop=true;
                break;
            }
            char target = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++){
                if (i == strs[j].length()){
                    stop=true;
                    break;
                }else{
                    if (strs[j].charAt(i) != target){
                    stop = true;
                    break;
                }
                }
            }
            if (!stop){
                result += target;
            }
            i++;
        }
        return result;
    }
}