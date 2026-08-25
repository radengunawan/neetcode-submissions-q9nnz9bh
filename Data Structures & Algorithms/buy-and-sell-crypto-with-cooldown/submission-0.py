class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp1_buy, dp1_sell = 0, 0
        dp2_buy = 0

        for i in range(n - 1, -1, -1):
            dp_buy = max(dp1_sell - prices[i], dp1_buy)
            dp_sell = max(dp2_buy + prices[i], dp1_sell)
            dp2_buy = dp1_buy
            dp1_buy, dp1_sell = dp_buy, dp_sell

        return dp1_buy