class Solution:
    def coinChange(self, coins: List[int], goal_amount: int) -> int:
        INF = 2**31
        dp = [INF] * (goal_amount + 1)
        dp[0] = 0
        for amount in range(0, goal_amount + 1):
            for coin in coins:
                if amount - coin < 0:
                    break
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
                
        if dp[goal_amount] != INF:
            return dp[goal_amount]

        return -1