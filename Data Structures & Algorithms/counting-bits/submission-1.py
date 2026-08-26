class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        dp = [0] * (n + 1)
        dp[1] = 1
        i = 1
        bit = 0
        for num in range(2, n + 1):
            dp[num] = dp[i]
            if bit == 1:
                dp[num] += 1
                i += 1
            bit = 1 - bit
        return dp


        