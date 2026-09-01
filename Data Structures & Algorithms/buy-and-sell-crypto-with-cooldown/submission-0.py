class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        h_prev1 = -prices[0]
        e_prev1 = 0
        e_prev2 = 0

        for price in prices[1:]:
            h_curr = max(h_prev1, e_prev2 - price)
            e_curr = max(e_prev1, h_prev1 + price)

            # Slide window forward for next iteration
            e_prev2 = e_prev1
            e_prev1 = e_curr
            h_prev1 = h_curr

        return e_prev1 