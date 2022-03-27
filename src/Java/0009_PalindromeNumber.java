class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }else{
            int length = 0;
            int y = x;
            while (y > 0){
                length ++;
                y = y/10;
            }
            int[] list = new int[length];
            y = x;
            length = 0;
            while (y>0){
                list[length] = y % 10;
                y = y/10;
                length++;
            }
            int i = 0;
            int j = length-1;
            while (i<j){
                if (list[i] == list[j]){
                    i++;
                    j--;
                }else{
                    return false;
                }
            }
            return true;
        }
    }
}