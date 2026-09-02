from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)

        # dp[l][r] stores the max coins obtained by bursting all balloons (the open interval (l, r))
        dp = [[0] * n for _ in range(n)]


        for length in range(2, n):
            for l in range(0, n - length):
                r = l + length

                # Try every balloon k in (l, r) as the LAST balloon to burst in this interval
                max_coins = 0
                for k in range(l + 1, r):
                    coins = dp[l][k] + dp[k][r] + arr[l] * arr[k] * arr[r]
                    if coins > max_coins:
                        max_coins = coins

                dp[l][r] = max_coins

        return dp[0][n - 1] 