class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1e6
        for i in range(n):
            p = 1
            for j in range(i, n):
                p *= nums[j]
                if p > ans:
                    ans = p
        return ans

        