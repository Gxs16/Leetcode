class Solution1475 {
    public int[] finalPrices(int[] prices) {
        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                if (prices[i] - prices[j] >= 0) {
                    prices[i] = prices[i] - prices[j];
                    break;
                }
            }
        }
        return prices;
    }
}