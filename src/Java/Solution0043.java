class Solution0043 {
    public String multiply(String num1, String num2) {
        if (num1.length() > num2.length()) {
            String tmp = num1;
            num1 = num2;
            num2 = tmp;
        }
        String res = "0";
        for (int i = 0; i < num1.length(); i++) {

            StringBuilder tmp = new StringBuilder(multiplyOne(num2, num1.charAt(num1.length() - i - 1) - '0'));
            for (int j = 0; j < i; j++) {
                tmp.append("0");
            }
            res = add(res, tmp.toString());
        }
        return res;
    }

    public String multiplyOne(String num1, int digit) {
        if (digit == 0) {
            return "0";
        }
        StringBuilder res = new StringBuilder();
        int add = 0;
        for (int i = 0; i < num1.length(); i++) {
            int d = (num1.charAt(num1.length() - i - 1) - '0') * digit + add;
            if (d >= 10) {
                add = d / 10;
                d -= (add * 10);
            } else {
                add = 0;
            }
            res.insert(0, d);
        }
        if (add > 0) {
            res.insert(0, add);
        }
        return res.toString();
    }

    public String add(String num1, String num2) {
        int length = Math.max(num1.length(), num2.length());
        StringBuilder res = new StringBuilder();
        int add = 0;
        for (int i = 0; i < length; i++) {
            int c1 = 0;
            int c2 = 0;
            if (i < num1.length()) {
                c1 = num1.charAt(num1.length() - i - 1) - '0';
            }
            if (i < num2.length()) {
                c2 = num2.charAt(num2.length() - i - 1) - '0';
            }
            int d = c1 + c2 + add;
            if (d >= 10) {
                add = 1;
                d -= 10;
            } else {
                add = 0;
            }
            res.insert(0, d);
        }
        if (add > 0) {
            res.insert(0, add);
        }
        return res.toString();
    }
}
