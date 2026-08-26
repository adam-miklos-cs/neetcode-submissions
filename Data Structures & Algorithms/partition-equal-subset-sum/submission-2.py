class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        t = s // 2
        dp = [False] * (t + 1)
        dp[0] = True
        for num in nums:
            for j in range(t, num - 1, -1):
                dp[j] = dp[j] | dp[j - num]
        
        return dp[t]

        