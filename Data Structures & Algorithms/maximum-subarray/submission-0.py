class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -1e6 - 1
        s = 0
        for i in range(len(nums)):
            if s + nums[i] < 0:
                s = 0
                ans = max(ans, nums[i])
            else:
                s += nums[i]
                ans = max(ans, s)
        
        return ans

       
    