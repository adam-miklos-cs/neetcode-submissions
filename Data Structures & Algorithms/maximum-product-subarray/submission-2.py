class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = nums[0]
        mini = nums[0]
        ans = nums[0]
        for i in range(1, n):
            continue_max = maxi * nums[i]
            continue_min = mini * nums[i]
            maxi = max(nums[i], continue_max, continue_min)
            mini = min(nums[i], continue_max, continue_min)
            ans = max(ans, maxi)

        return ans

        