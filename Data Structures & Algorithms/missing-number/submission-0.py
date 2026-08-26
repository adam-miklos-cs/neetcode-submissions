class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(0, n + 1):
            res ^= i
        for num in nums:
            res ^= num
        return res

        