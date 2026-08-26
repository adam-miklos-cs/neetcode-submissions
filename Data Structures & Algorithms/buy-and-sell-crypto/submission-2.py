class Solution:
    def maxProfit(self, p: List[int]) -> int:
        n = len(p)
        i, j = 0, 1
        profit = 0
        while j < n:
            if p[i] <= p[j]:
                profit = max(profit, p[j] - p[i])
                j = j + 1
            else:
                i = j
        return profit

        