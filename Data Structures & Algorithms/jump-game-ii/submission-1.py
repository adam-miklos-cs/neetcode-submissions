class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        dp = [0] * (n + 1)
        j = 1
        dp[j] = 0 + nums[0]
        if dp[j] >= n - 1:
            return j
        for i in range(1, n):
            if dp[j] < i:
                j += 1
                if dp[j] >= n - 1:
                    return j
            dp[j + 1] = max(dp[j + 1], i + nums[i])
        



